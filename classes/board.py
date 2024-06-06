from shape_data import shapes_dict, get_variant_conversion
import secrets


class Board:

    def __init__(self, width, height, shapes=[]):
        self.id = "board_" + secrets.token_hex(8)
        self.width = width
        self.height = height
        self.shapes = {shape: shapes_dict[shape] for shape in shapes} # Some games will feature changing valid shapes, so need a method to handle that
        self.spaces = 0
        def get_num():
            self.spaces += 1
            return self.spaces
        self.board = [[[get_num(), '.', []] for x in range(width)] for y in range(height)]

    def get_coordinates(self, space):
        row = (int(space) - 1) // self.width
        col = (int(space) - 1) % self.width
        print('Row:', row, 'Col:', col)
        return row, col

    def move(self, space, player):
        row, col = self.get_coordinates(space)
        if self.board[row][col][1] == '.':
            self.board[row][col][1] = player
            self.check(row, col, player)
        else:
            return {'success': False, 'message': 'Space already taken'} # Will implement method to check further
        return {'success': True}

    def check(self, row, col, player):
        for shape in self.shapes:
            print('Checking shape:', shape)
            shape_data = self.shapes[shape]
            if 'coordinates' in shape_data: # Might not need this if statement (or might)
                start_row = row - (shape_data['height'] - 1)
                start_col = col - (shape_data['width'] - 1)
                footprints = []
                for variant in shape_data['variants'].split():
                    converted_coordinates = get_variant_conversion(variant, shape_data) # ALSO NEEDS TO GET THE NEW HEIGHT AND WIDTH
                    print('Converted coordinates:', converted_coordinates)
                for i in range(shape_data['height']):
                    for j in range(shape_data['width']):
                        footprint = [((start_row + y) + i, (start_col + x) + j) for y, x in shape_data['coordinates']]
                        if any(space[0] < 0 or space[0] >= self.height or space[1] < 0 or space[1] >= self.width for space in footprint):
                            continue
                        footprints.append(footprint)
                print('Footprints:', footprints)
                for footprint in footprints:
                    if all(self.board[space[0]][space[1]][1] == player for space in footprint):
                        print('Match')
                        # Upon a match a class object will be created to store the winning shape data
                        # The class object will be used to prevent previous matches from being counted again
                    else:
                        print('No match')
            
