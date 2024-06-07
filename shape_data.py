shapes_dict = {
    'standard_line': {
        'dimensions': "get_line",
        'variants': "r0 r1",
        'messages': [
            "lay down {q} perfectly horizontal line{p} of",
            "hung {q} terrifyingly vertical line{p} of"
        ]
    },
    'diagonal_line': {
        'dimensions': "get_line",
        'variants': "r0 f0",
        'messages': [
            "drew {q} diagonal line{p} of",
            "sketched {q} diagonal line{p} of"
        ]
    },
    'square': {
        'width': 2,
        'height': 2,
        'variants': "r0 e1",
        'coordinates': [(0, 0), (0, 1), (1, 0), (1, 1)],
        'messages': [
            "built {q} robust square{p}",
            "discovered the magic corners of {qv} almost invisible square{p}"
        ]
    },
    'diamond': {
        'width': 3,
        'height': 3,
        'variants': "r0 e2",
        'coordinates': [(0, 1), (1, 0), (1, 2), (2, 1)],
        'messages': [
            "dug up {q} shiny diamond{p}",
            "dug up from the ground the sparkling corners of {q} never before seen diamond{p}"
        ]
    },
    'corners': {
        'dimensions': "get_board",
        'variants': "c0 cr",
        'messages': [
            "cast a spell producing the magic corners of the board",
            "cast a spell revealing the majestically rotating corners of the board"
        ]
    },
    'l_shape': {
        'width': 2,
        'height': 3,
        'variants': "r0 r1 r2 r3 f0 f1 f2 f3",
        'coordinates': [(0, 0), (1, 0), (2, 0), (2, 1)],
        'messages': [
            "made {q} perfect representation{p} of the letter L",
            "formed {q} rotated L{p}",
            "hung {qv} upside down L{p}",
            "demonstrated {q} lying down L{p}",
            "painted {q} brilliantly reversed L{p}",
            "found {qv} odd lying down L{p}",
            "spun up {qv} extremely dizzy L{p}",
            "drew {q} pretty cool reversed L{p}"
        ]
    },
    'stumpy_t': {
        'width': 3,
        'height': 2,
        'variants': "r0 r1 r2 r3",
        'coordinates': 'abce',
        'messages': [
            "created {q} T shape{p}",
            "built {q} T{p}",
            "made {q} T{p}",
            "constructed {q} T{p}"
        ]
    },
    'short_lightning': {
        'width': 2,
        'height': 3,
        'variants': "r0 r1 f0 f1",
        'coordinates': 'acdf',
        'messages': [
            "produced {q} powerful lightning strike{p} from the northwestern sky",
            "produced {q} powerful lightning bolt{p} from the western sky",
            "conjured {q} magical lightning bolt{p} from the northwest",
            "summoned {q} lightning bolt{p} from the east"
        ]
    },
    'horseshoe': {
        'width': 3,
        'height': 2,
        'variants': "r0 r1 r2 r3",
        'coordinates': 'abcdf',
        'messages': [
            "crafted {q} sturdy horseshoe{p}",
            "drew {q} slanted horseshoe{p}",
            "stumbled upon {qv} upside down horseshoe{p}",
            "crafted {q} brilliant horseshoe{p} on {t} side{p}"
        ]
    },
    'turning_line': {
        'width': 3,
        'height': 3,
        'variants': "r0 r1 r2 r3",
        'coordinates': 'adghi',
        'messages': [
            "sighted and reported the hands of {q} clock{p} bang on 3 o'clock",
            "sighted and reported the hands of {q} clock{p} at almost a quarter past 6",
            "sighted and reported the hands of {q} clock{p} at almost a quarter to 9",
            "sighted and reported the hands of {q} clock{p} bang on 9 o'clock"
        ]
    },
    'zigzag_5': {
        'width': 3,
        'height': 3,
        'variants': "r0 r1 r2 r3",
        'coordinates': 'adehi',
        'messages': [
            "drew {q} sharp meandering zigzag{p} heading southeast",
            "drew {q} sharp meandering zigzag{p} heading northeast",
            "drew {q} sharp meandering zigzag{p} heading northwest",
            "drew {q} sharp meandering zigzag{p} heading southwest"
        ]
    },
    'funny_shape': {
        'width': 3,
        'height': 3,
        'variants': "r0 r1 f0 f1",
        'coordinates': 'abehi',
        'messages': [
            "came across {qv} indescribably funny shape{p} in {t} apparently original form{p}",
            "came across {qv} indescribably funny shape{p} in {t} apparently first rotation{p}",
            "came across {qv} indescribably funny shape{p} in {t} apparently reversed form{p}",
            "came across {qv} indescribably funny shape{p} in {t} apparently most odd form{p}"
        ]
    },
    'cross': {
        'width': 3,
        'height': 3,
        'variants': "r0",
        'coordinates': 'acegi',
        'messages': [
            "slammed down {q} powerful cross{pe}"
        ]
    },
    'plus': {
        'width': 3,
        'height': 3,
        'variants': "r0",
        'coordinates': 'bdefh',
        'messages': [
            "made {q} powerful addition{p}"
        ]
    }
}

def get_variant_conversion(variant, shape_data):
    original_width = shape_data['width']
    original_height = shape_data['height']
    original_coordinates = shape_data['coordinates']

    def normalize_coordinates(coords):
        min_x = min(x for x, y in coords)
        min_y = min(y for x, y in coords)
        return [(x - min_x, y - min_y) for x, y in coords]
    
    def flip_coordinates(coords):
        return [(x, original_height - 1 - y) for x, y in coords]

    if variant == 'r0':
        rotated_coordinates = original_coordinates
    elif variant == 'r1': # 90 degrees clockwise
        rotated_coordinates = [(y, original_width - 1 - x) for x, y in original_coordinates]
    elif variant == 'r2': # 180 degrees clockwise
        rotated_coordinates = [(original_width - 1 - x, original_height - 1 - y) for x, y in original_coordinates]
    elif variant == 'r3': # 270 degrees clockwise
        rotated_coordinates = [(original_height - 1 - y, x) for x, y in original_coordinates]
    elif variant == 'f0': # Flip horizontally
        rotated_coordinates = flip_coordinates(original_coordinates)
    elif variant == 'f1': # Flip horizontally and rotate 90 degrees clockwise
        rotated_coordinates = [(y, original_width - 1 - x) for x, y in flip_coordinates(original_coordinates)]
    elif variant == 'f2': # Flip horizontally and rotate 180 degrees clockwise
        rotated_coordinates = [(original_width - 1 - x, original_height - 1 - y) for x, y in flip_coordinates(original_coordinates)]
    elif variant == 'f3': # Flip horizontally and rotate 270 degrees clockwise
        rotated_coordinates = [(original_height - 1 - y, x) for x, y in flip_coordinates(original_coordinates)]
    # Add variants for e1, e2, c0, cr

    return normalize_coordinates(rotated_coordinates)
