# build123d Workspace

A streamlined workspace for parametric CAD modeling with build123d. I wanted a convenient workflow with auto-rendering and one-click export in Cursor/VSCode, where I can focus on writing geometry code while `boot.py` handles imports, visualization, and export.

This serves as a shared workspace for all my build123d projects and libraries — just write geometry, everything else is automated.

## Installation

### Required Extensions

- **OCP CAD Viewer** (`ocp-vscode`) - 3D visualization
- **Run on Save** (`emeraldwalk.RunOnSave`) - Auto-render on file save
- **VsCodeTaskButtons** - Status bar buttons for render/export in the bottom of the screen

## Features

### Auto-Import System

No imports needed in your scripts—`boot.py` auto-injects all build123d symbols, just write geometry directly inside your project/main.py files.

Make sure to pass resulting geometry to the `result` variable, so `boot.py` can automatically detect it and render it in the OCP viewer.

### Viewer Defaults

Pre-configured OCP viewer settings:
- Camera reset disabled
- No axes, grid, transparency slider, or logo
- Clean visualization focused on your model

### Workspace Layout

- Left editor group: Python scripts
- Right editor group: OCP CAD Viewer (auto-opens in column 2)
- Backend terminal hidden (auto-starts in background)

