from shape_data import shapes_dict, get_variant_conversion
from classes.shape import Shape
import secrets


class Board:

    def __init__(self, width, height, shapes=[], players=[]):
        self.id = "board_" + secrets.token_hex(8)
        self.width = width
        self.height = height
        self.shapes = {shape: shapes_dict[shape] for shape in shapes} # Some games will feature changing valid shapes, so need a method to handle that
        self.spaces = 0
        def get_num():
            self.spaces += 1
            return self.spaces
        self.board = [[[get_num(), '.', []] for x in range(width)] for y in range(height)]
        self.players = players

    def get_coordinates(self, space):
        row = (int(space) - 1) // self.width
        col = (int(space) - 1) % self.width
        print('Row:', row, 'Col:', col)
        return row, col

    def move(self, space, player):
        row, col = self.get_coordinates(space)
        if self.board[row][col][1] == '.':
            self.board[row][col][1] = player
            new_shapes = self.check(row, col, player)
        else:
            return {'success': False, 'message': 'Space already taken'} # Will implement method to check further
        return {'success': True, 'new_shapes': new_shapes}

    def check(self, row, col, player):
        for shape in self.shapes:
            shape_data = self.shapes[shape]
            if 'coordinates' not in shape_data:
                pass # Generate coordinates for shape (lines and corners)
            count = 0 # Increment this at the end of the loop
            for variant in shape_data['variants'].split():
                # For certain games with changing valid shapes, a variant void list will need to be be checked here
                width, height, coordinates = get_variant_conversion(
                    variant, shape_data['width'], shape_data['height'], shape_data['coordinates'], self.width, self.height
                )
                start_row, start_col = row - (height - 1), col - (width - 1)
                footprints = []
                # print('Converted coordinates:', coordinates)
                # print('Width:', width, 'Height:', height)
                for i in range(height):
                    for j in range(width):
                        footprint = [((start_row + y) + i, (start_col + x) + j) for y, x in coordinates]
                        if any(space[0] < 0 or space[0] >= self.height or space[1] < 0 or space[1] >= self.width for space in footprint):
                            continue
                        footprints.append(footprint)
                # print('Footprints:', footprints)
                for footprint in footprints:
                    if all(self.board[space[0]][space[1]][1] == player for space in footprint):
                        print('Match')
                        print('Footprint:', footprint)
                        print('variant', variant)
                        
                        player_object = next(player_ for player_ in self.players if player_.character == player)
                        shape_exists = False
                        for made_shape in player_object.shapes:
                            if made_shape.coordinates == footprint:
                                print('Shape already exists')
                                shape_exists = True
                                break
                        if not shape_exists:
                            try: # !!! This may not be needed as a method to add the messages on will be implemented
                                new_shape = Shape(shape, variant, shape_data['messages'][count], footprint)
                            except IndexError:
                                new_shape = Shape(shape, variant, shape_data['messages'][-1], footprint)
                            print(new_shape)
                            player_object.shapes.append(new_shape)
                        
                        
                        
                        # Upon a match a class object will be created to store the winning shape data
                        # The class object will be used to prevent previous matches from being counted again
                    else:
                        pass
                        # print('No match for this')
                count += 1
