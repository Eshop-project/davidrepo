# Milestone 3. Core Features Implemented - Design
PROJECT INFO
Software Project Plan - Eshop Ecommerce website

Other Roles - Requirements.md , Design.md , Code.md , Test.md

File: Milestone-3/Design.md

Website URL: https://eshopproject.pythonanywhere.com/

URL: https://github.com/Eshop-project/CS-350/edit/master/docs/plan/Milestone_3/Design.md

Documents: https://github.com/Eshop-project/CS-350/tree/master/docs/plan

Git Repo: https://github.com/Eshop-project/CS-350

## Milestone 3. Core Features Implemented
Role: Designer Bryan Aguilar - Design

Goal: Component Design - API

### Prototype - development spike of core functionality

Implement data models- In our data model we have 6 models that store all of the information needed for the Eshop Website.  The models are show below in this diagram.

![image info](model.png)

Implement views- 

For the views we have a admin view that allows the Superuser to login into to see orders, edit orders and add Items. This view is to be used by site personal only.  The Store view displays all the items we have for sale.  The Cart view displays all items in shopping cart.  There is a Checkout view that totals up cart price and conducts final transaction.  Three more views are need but not finished which include Order, Success and Registration.

Implement URL routes-

Admin View- https://eshopproject.pythonanywhere.com/admin/login/?next=/admin/

Store View- https://eshopproject.pythonanywhere.com/ 

Shopping Cart- https://eshopproject.pythonanywhere.com/cart/

Checkout- https://eshopproject.pythonanywhere.com/checkout/
