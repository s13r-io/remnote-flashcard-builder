# Calculus: Foundations and Key Concepts

## What is Calculus?

Calculus is the branch of mathematics that studies continuous change. It was independently developed by Isaac Newton and Gottfried Wilhelm Leibniz in the late 17th century. Calculus has two major branches: differential calculus, which studies rates of change and slopes of curves, and integral calculus, which studies accumulation of quantities and areas under curves. Calculus is fundamental to physics, engineering, economics, and many other fields.

## Limits

A limit describes the value that a function approaches as the input approaches a given value. The notation lim(x→a) f(x) = L means that as x gets closer to a, f(x) gets closer to L. A limit exists only if the left-hand limit and the right-hand limit are equal. Limits are the foundation of both derivatives and integrals. A function is continuous at a point if the limit at that point equals the function's value there.

## Derivatives

The derivative of a function measures its instantaneous rate of change at a given point. It is defined as the limit of the difference quotient: f'(x) = lim(h→0) [f(x+h) - f(x)] / h. Geometrically, the derivative at a point gives the slope of the tangent line to the curve at that point. The process of finding a derivative is called differentiation. Common notation includes f'(x), dy/dx (Leibniz notation), and Df (operator notation).

## Basic Differentiation Rules

The power rule states that the derivative of x^n is nx^(n-1). The constant rule states that the derivative of a constant is zero. The sum rule states that the derivative of a sum equals the sum of the derivatives. The product rule states that (fg)' = f'g + fg'. The chain rule is used for composite functions: if y = f(g(x)), then dy/dx = f'(g(x)) · g'(x). The quotient rule states that (f/g)' = (f'g - fg') / g².

## Applications of Derivatives

Derivatives have many practical applications. In physics, velocity is the derivative of position with respect to time, and acceleration is the derivative of velocity. Critical points occur where f'(x) = 0 or f'(x) is undefined. The first derivative test determines whether a critical point is a local maximum, local minimum, or neither. The second derivative test uses concavity: if f''(x) > 0 the function is concave up (local minimum), and if f''(x) < 0 it is concave down (local maximum).

## Integrals

Integration is the reverse process of differentiation. The indefinite integral (antiderivative) of f(x) is written as ∫f(x)dx and represents a family of functions differing by a constant C. The definite integral ∫[a to b] f(x)dx calculates the net area between the curve and the x-axis from x = a to x = b. Areas above the x-axis are positive, and areas below are negative.

## The Fundamental Theorem of Calculus

The Fundamental Theorem of Calculus connects differentiation and integration. Part 1 states that if F(x) = ∫[a to x] f(t)dt, then F'(x) = f(x). Part 2 states that ∫[a to b] f(x)dx = F(b) - F(a), where F is any antiderivative of f. This theorem shows that differentiation and integration are inverse operations and provides a practical method for evaluating definite integrals.

## Common Integration Techniques

Basic integration techniques include the power rule for integration: ∫x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1). Substitution (u-substitution) reverses the chain rule by replacing a composite expression with a single variable. Integration by parts reverses the product rule: ∫u dv = uv - ∫v du. Partial fractions decompose rational functions into simpler fractions that can be integrated individually.
