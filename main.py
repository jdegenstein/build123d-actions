# add or adjust any necessary imports:
from build123d import *

# KEEP custom export_all method:
from build123d import Shape
def export_all(shape: Shape, base_filename: str = "export_"):
    import datetime

    # Get the current time
    now = datetime.datetime.now()
    base_timestamped = base_filename + now.strftime('%Y%m%d%H%M%S')

    for func, ext in zip((export_step, export_stl, export_brep, export_gltf),(".step", ".stl", ".brep", ".gltf")):
        func(shape, base_timestamped + ext)

    for cls, ext in zip((ExportSVG, ExportDXF, Mesher), (".svg", ".dxf", ".3mf")):
        try:
            exporter = cls()
            exporter.add_shape(shape)
            exporter.write(base_timestamped + ext)
        except:
            print(f"Export failed using: {cls.__name__}")
    
    # TODO: consider STL via Mesher

############## add your model generation here: ##################
pts = [
    (55, 30),
    (50, 35),
    (40, 30),
    (30, 20),
    (20, 25),
    (10, 20),
    (0, 20),
]

with BuildPart() as ex12:
    with BuildSketch() as ex12_sk:
        with BuildLine() as ex12_ln:
            l1 = Spline(pts)
            l2 = Line((55, 30), (60, 0))
            l3 = Line((60, 0), (0, 0))
            l4 = Line((0, 0), (0, 20))
        make_face()
    extrude(amount=10)


################ export the correct object: #####################
export_all(shape=ex12.part)



