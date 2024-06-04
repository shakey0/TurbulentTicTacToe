patterns = {
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
        'coordinates': 'abcd',
        'messages': [
            "built {q} robust square{p}",
            "discovered the magic corners of {qv} almost invisible square{p}"
        ]
    },
    'diamond': {
        'width': 3,
        'height': 3,
        'variants': "r0 e2",
        'coordinates': 'bdfh',
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
        'coordinates': 'acef',
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
    'stumpy_t_shape': {
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
    'lightning_shape': {
        'width': 2,
        'height': 3,
        'variants': "r0 r1 f0 f1",
        'coordinates': 'abde',
        'messages': [
            "produced {q} powerful lightning strike{p} from the northwestern sky",
            "produced {q} powerful lightning bolt{p} from the western sky",
            "conjured {q} magical lightning bolt{p} from the northwest",
            "summoned {q} lightning bolt{p} from the east"
        ]
    },
}
