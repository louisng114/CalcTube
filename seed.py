from models import Topic, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

topics = [
    Topic(
        name="Overview",
        description="The idea of calculus in broad stokes"
        ),
    Topic(
        name="Limits and Continuity",
        description="""How limits help us to handle change at an instant; \n
            Definition and properties of limits in various representations; \n
            Definitions of continuity of a function at a point and over a domain; \n
            Asymptotes and limits at infinity; \n
            Reasoning using the Squeeze theorem and the Intermediate Value Theorem
            """
        ),
    Topic(
        name="Differentiation: Definition and Fundamental Properties",
        description="""Defining the derivative of a function at a point and as a function; \n
            Connecting differentiability and continuity; \n
            Determining derivatives for elementary functions; \n
            Applying differentiation rules
            """
        ),
    Topic(
        name="Differentiation: Composit, Implicit, and Inverse Functions",
        description="""The chain rule for differentiating composite functions; \n
            Implicit differentiation; \n
            Differentiation of general and particular inverse functions; \n
            Determining higher-order derivatives of functions
            """
        ),
    Topic(
        name="Contextual Application of Differentiation",
        description="""Identifying relevant mathematical information in verbal representations of real-world problems involving rates of change; \n
            Applying understandings of differentiation to problems involving motion; \n
            Generalizing understandings of motion problems to other situations involving rates of change; \n
            Solving related rates problems; \n
            Local linearity and approximation; \n
            L’Hospital’s rule
            """
        ),
    Topic(
        name="Analytical Application of Differentiation",
        description="""Mean Value Theorem and Extreme Value Theorem; \n
            Derivatives and properties of functions; \n
            How to use the first derivative test, second derivative test, and candidates test; \n
            Sketching graphs of functions and their derivatives; \n
            How to solve optimization problems; \n
            Behaviors of Implicit relations
            """
        ),
    Topic(
        name="Integration and Accumulation of Change",
        description="""Using definite integrals to determine accumulated change over an interval; \n
            Approximating integrals using Riemann Sums; \n
            Accumulation functions, the Fundamental Theorem of Calculus, and definite integrals; \n
            Antiderivatives and indefinite integrals; \n
            Properties of integrals and integration techniques
            """
        ),
    Topic(
        name="Differential Equations",
        description="""Interpreting verbal descriptions of change as separable differential equations; \n
            Sketching slope fields and families of solution curves; \n
            Solving separable differential equations to find general and particular solutions; \n
            Deriving and applying a model for exponential growth and decay
            """
        ),
    Topic(
        name="Differential Equations (BC Only)",
        description="""Using Euler’s method to approximate values on a particular solution curve
            """
        ),
    Topic(
        name="Applications of Integration",
        description="""Determining the average value of a function using definite integrals; \n
            Modeling particle motion; \n
            Solving accumulation problems; \n
            Finding the area between curves; \n
            Determining volume with cross-sections, the disc method, and the washer method
            """
        ),
    Topic(
        name="Applications of Integration (BC Only)",
        description="""Determining the length of a planar curve using a definite integral
            """
        ),
    Topic(
        name="Parametric Equations, Polar Coordinates, and Vector-Valued Functions (BC Only)",
        description="""Finding derivatives of parametric functions and vector-valued functions; \n
            Calculating the accumulation of change in length over an interval using a definite integral; \n
            Determining the position of a particle moving in a plane; \n
            Calculating velocity, speed, and acceleration of a particle moving along a curve; \n
            Finding derivatives of functions written in polar coordinates; \n
            Finding the area of regions bounded by polar curves
            """
        ),
    Topic(
        name="Infinite Sequences and Series (BC Only)",
        description="""Applying limits to understand convergence of infinite series; \n
            Types of series: Geometric, harmonic, and p-series; \n
            A test for divergence and several tests for convergence; \n
            Approximating sums of convergent infinite series and associated error bounds; \n
            Determining the radius and interval of convergence for a series; \n
            Representing a function as a Taylor series or a Maclaurin series on an appropriate interval
            """
        ),
    Topic(
        name="Exam Information",
        description="Information about the AP exam"
        ),
]

with app.app_context():
    db.session.add_all(topics)
    db.session.commit()