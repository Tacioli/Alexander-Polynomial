# User MANUAL -  A web application that calculates the Alexander polynomial via PyScript


This manual provides a comprehensive guide for users to understand and effectively utilize the web application, to draw knot diagrams and calculate their corresponding Alexander polynomials. 

## Key Features and Functionalities:

1.  **Interactive Diagram Creation:**

    *   Users can  draw knot diagrams directly on the canvas by clicking to establish vertices and connecting them with line segments.
    *   The interface dynamically labels each vertex as it is created, enhancing visual clarity and reference during the drawing process.
    *   To close the diagram, the user must move the mouse over the first vertex. A dedicated modal dialog, the ``Close Knot" dialog (Figure \ref{Fig1}), prompts users to confirm the completion of their knot diagram. Upon confirmation, the script seamlessly connects the final vertex to the initial vertex, ensuring a closed loop structure that is fundamental to knot theory.

2.  **Intersection Detection and Resolution:**

    *   The script identifies and visually highlights points where line segments intersect within the knot diagram.
    *   Through an interactive process, users are asked to choose which segment should pass over the other at each crossing point (Figure \ref{Fig2}). Visual aids, such as a blinking dot and highlighted segments, assist users in making these critical decisions.

3.  **Alexander Polynomial Calculation:**

    *   Once the knot diagram is finalized and all crossing relationships are established, the ``Alexander Polynomial" button becomes active.
    *   Clicking this button initiates the execution of a Python script (`main.py') embedded within the HTML using \href{https://pyodide.org/en/stable/}{Pyodide} and \href{https://pyscript.net/}{PyScript}. After the calculation, the application displays the determinant, {\bf D $= |p(-1)|$}, and the Alexander polynomial, $p(t)$, see Figure \ref{Fig3}. ![Figure 1. Knot diagram.](https://github.com/Tacioli/Alexander-Polynomial/blob/main/Close%20diagram.png)
    <figure>
       <img src="https://github.com/Tacioli/Alexander-Polynomial/blob/main/Close%20diagram.png" alt="Um lindo pôr do sol">
       <figcaption>Figure 1. Knot diagram.</figcaption>
    </figure>
    *   If the user wants to change any intersection, just click on the intersection with the mouse to swap the choice.

4.  **Diagram Persistence:**

    *   The ``Save Diagram" button allows users to preserve their work by saving the current knot diagram to a \verb".txt" file. This file stores both the vertex coordinates and the crossing choices made by the user.
    *   The ``Load Diagram" button enables users to retrieve previously saved diagrams, fostering continued analysis, modification, or comparison.

5.  **Intalling:**

    *   Click in the link \href{https://tacioli.github.io/Alexander-Polynomial/}{https://tacioli.github.io/Alexander-Polynomial/} to use the application.

6.  **User-Friendly Interface:**

    *   The interface is built using Bootstrap, ensuring a clean, organized, and responsive layout.
    *   Interactive buttons trigger actions, while text element display the calculated Alexander polynomial.
    *   A ``Help" button reveals a set of instructions, guiding users on how to effectively utilize the application's features.
    *   The ``New knot" button clears the canvas.

## Additional Technical Details:

*   Buttons are dynamically enabled or disabled based on the current state of the knot diagram (e.g., the ``Alexander Polynomial" button remains disabled until the diagram is closed and all crossings are resolved).
*   The script continuously updates a display element to show the current mouse coordinates as the user interacts with the canvas.
*   Open only files in \verb|.txt| format.
*   When separately creating a \verb|.txt| file of a diagram of a knot, make sure not to create blank lines.




