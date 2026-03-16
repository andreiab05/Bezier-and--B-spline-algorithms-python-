# Bezier and B-Spline algorithms (Python)

## Overview
This project contains Python implementations of several algorithms used in geometric modeling and computer graphics.  
The programs compute points on Bezier curves, rational Bezier curves, B-Spline curves, and Bezier surfaces using classical algorithms such as De Casteljau and De Boor.

The project was developed as part of the *Applications of Geometry in Computer Science* course.

## Implemented Algorithms
- De Casteljau algorithm for Bezier curves
- Derivative computation for Bezier curves
- Rational Bezier curves
- Bezier surfaces
- Triangular Bezier surfaces
- Extruded surfaces from cubic Bezier curves
- De Boor algorithm for B-Spline curves
- Geometric transformations (polygon reflection)

## Technologies
- Python
- NumPy
- Matplotlib

## Files
- `punctCurbaBezier.py` – point evaluation on a Bezier curve
- `punctCurbaBezierBigrad.py` – Bezier curve and derivative computation
- `punctCurbaBezierRationala.py` – rational Bezier curves with visualization
- `punctSuprafataBezierTriunghiulara.py` – triangular Bezier surface
- `pctSprfBezierCubicaExtrudata.py` – extruded Bezier surface
- `de_Boor.py` – B-Spline evaluation using the De Boor algorithm
- `relfexiePoligon.py` – geometric transformations of polygons

## How to Run
Example:

```bash
python punctCurbaBezier.py
