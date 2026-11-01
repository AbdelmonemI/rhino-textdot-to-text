"""
TextDot to Text
Rhino 8 (Python 3) - run in ScriptEditor or with _-RunPythonScript

Converts every TextDot in the model to a Text object at the same point.
DWG and DXF do not support TextDots, so the exporter drops them.
Text objects export correctly.

The new Text objects go on a separate layer. The original TextDots stay
in place. Hide or delete them before you export.
"""
import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc
import System

TARGET_LAYER = "TextDot_Export"
TEXT_HEIGHT = 1.0  # model units - adjust to your print scale
FONT = "Arial"


def main():
    if not rs.IsLayer(TARGET_LAYER):
        rs.AddLayer(TARGET_LAYER)

    dot_ids = rs.ObjectsByType(rs.filter.textdot)
    count = 0

    for dot_id in dot_ids or []:
        dot = sc.doc.Objects.Find(dot_id).Geometry
        plane = Rhino.Geometry.Plane(dot.Point, Rhino.Geometry.Vector3d.ZAxis)
        new_id = sc.doc.Objects.AddText(dot.Text, plane, TEXT_HEIGHT, FONT, False, False)
        if new_id != System.Guid.Empty:
            rs.ObjectLayer(new_id, TARGET_LAYER)
            count += 1

    sc.doc.Views.Redraw()
    print("Converted {} TextDots to Text.".format(count))


if __name__ == "__main__":
    main()
