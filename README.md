# Analysis of HTML Code for Alexander Polynomial Calculation

# Installing

Click in the ling https://tacioli.github.io/Alexander-Polynomial/ to use the application.

This HTML code is designed to create an interactive web application that empowers users to explore the fascinating world of knot theory. Its primary function is to facilitate the drawing of knot diagrams and the automated calculation of their corresponding Alexander polynomials. The Alexander polynomial is a crucial knot invariant used to distinguish and classify different types of knots, making it a cornerstone of topological studies.

## Key Features and Functionalities:

1.  **Interactive Diagram Creation:**

    *   Users can intuitively draw knot diagrams directly on the canvas by clicking to establish vertices and connecting them with line segments.
    *   The interface dynamically labels each vertex as it's created, enhancing visual clarity and reference during the drawing process.

2.  **Closing the Knot:**

    *   A dedicated modal dialog, the "Close Knot" dialog, prompts users to confirm the completion of their knot diagram.
    *   Upon confirmation, the script seamlessly connects the final vertex to the initial vertex, ensuring a closed loop structure that is fundamental to knot theory.

3.  **Intersection Detection and Resolution:**

    *   The script intelligently identifies and visually highlights points where line segments intersect within the knot diagram.
    *   Through an interactive process, users are guided to specify the over/under relationship at each crossing point. This crucial information is essential for accurately representing the knot's topology.
    *   Visual aids, such as a blinking dot and highlighted segments, assist users in making these critical decisions.

4.  **Alexander Polynomial Calculation:**

    *   Once the knot diagram is finalized and all crossing relationships are established, the "Alexander Polynomial" button becomes active.
    *   Clicking this button initiates the execution of a Python script (`main.py`) embedded within the HTML using Pyodide and PyScript.
    *   Leveraging the power of the `sympy` library for symbolic mathematics, the Python script computes the Alexander polynomial based on the knot's structure and the user-defined crossing information.

5.  **Diagram Persistence:**

    *   The "Save Diagram" button empowers users to preserve their work by saving the current knot diagram to a text file. This file stores both the vertex coordinates and the crossing choices made by the user.
    *   Conversely, the "Load Diagram" button enables users to retrieve previously saved diagrams, fostering continued analysis, modification, or comparison.

6.  **User-Friendly Interface:**

    *   The interface is built using Bootstrap, ensuring a clean, organized, and responsive layout that adapts to different screen sizes and devices.
    *   Interactive buttons trigger actions, while text elements provide feedback, instructions, and display the calculated Alexander polynomial.
    *   A "Help" button reveals a set of instructions, guiding users on how to effectively utilize the application's features.

## Additional Technical Details:

*   **Error Handling:** The code incorporates error handling mechanisms to gracefully manage potential issues during file saving operations.
*   **Dynamic Button States:** Buttons are dynamically enabled or disabled based on the current state of the knot diagram (e.g., the "Alexander Polynomial" button remains disabled until the diagram is closed and all crossings are resolved).
*   **Real-time Mouse Coordinates:** The script continuously updates a display element to show the current mouse coordinates as the user interacts with the canvas.
*   **Code Structure and Comments:** The code is well-organized and includes comments to elucidate the purpose of different code sections and variables, enhancing readability and maintainability.

## Conclusion:

This HTML code represents a sophisticated and user-friendly tool for delving into the intricacies of knot theory. By seamlessly integrating interactive diagram creation, crossing resolution, and automated Alexander polynomial calculation, it empowers users to visualize, analyze, and gain deeper insights into the world of knots. The incorporation of Python through Pyodide and PyScript showcases the potential of web technologies to facilitate complex mathematical and scientific computations within a browser-based environment.


# Some instructions

### 1. Sketch diagram with left mouse click;

### 2. Move mouse to first point to be asked about close diagram;

### 3. Make choose to get knot diagram;

### 4. Click "Alexander Polynomial" button to calculate polynomial Alexander of knot;

### 5. The "Save diagram" button stores the cartesian coordinates of the vertex and the choices of the segments that passed over.




