"""a). High level module should not depend on low level modules. Both should depend on abstractions

b). Abstractions should not depend on details. Details should depend on abstractions.

If your code follows the Open-Closed Principle and Liskov Substitution Principle, then it will be implicitly aligned to be compliant to the Dependency Inversion Principle also.

By following the Open-Closed Principle, you create Interfaces that can be used to provide different high-level implementations. By following Liskov Substitution Principle you ensure that you can replace the low-level class objects with high-level class objects without causing any adverse effect on the application. Thus, by following these two principles you ensure that your high-level classes and low-level classes depend on interfaces. Hence you would implicitly follow the Dependency Inversion Principle."""

