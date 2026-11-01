# rhino-textdot-to-text

Rhino 8 script. It changes TextDots to Text objects, so they stay in a DWG or DXF export.

## Problem

DWG and DXF have no TextDot entity. The Rhino exporter drops all TextDots without a warning.

## What the script does

1. Finds all TextDots in the model.
2. Makes a Text object at each TextDot point (same text, world Z-up plane).
3. Puts the new Text objects on the layer `TextDot_Export`.

The original TextDots stay in the model.

## Requirements

- Rhino 8 (Python 3 in ScriptEditor)
- No other plug-ins

## Use

1. Open the Rhino model.
2. Type `ScriptEditor` and press Enter.
3. Open `textdot_to_text.py` and press F5.
4. Hide or delete the original TextDots.
5. Export to DWG or DXF.

To run it from the command line or an alias:

```
! _-RunPythonScript "C:\path\to\textdot_to_text.py"
```

## Settings

Set these constants at the top of the script:

| Name | Default | Use |
|---|---|---|
| `TARGET_LAYER` | `TextDot_Export` | Layer for the new Text objects |
| `TEXT_HEIGHT` | `1.0` | Text height in model units. Set it to match your print scale. |
| `FONT` | `Arial` | Font name |

## Limits

- Text lies flat on the XY plane. TextDots in 3D views do not keep screen-facing behavior.
- Text height is the same for all dots. TextDots have no height of their own.
- The script does not copy layer, color, or user text from the TextDot.

## Licence

MIT
