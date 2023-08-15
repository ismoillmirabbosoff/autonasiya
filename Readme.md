
# Auto Nasiya Project

The Auto Nasiya project automates the management of Nasiya products, streamlining customer purchases, payments, and financial tracking. This README provides a brief guide on using the project effectively.

## Getting Started

To use the Auto Nasiya project, follow these steps:

1.  **Setting Up Environment:**
    
    -   Make sure you have Python and Django installed on your system.
    -   Clone the project repository.
2.  **Configuring the Database:**
    
    -   Configure your database settings in `settings.py`.
3.  **Running Migrations:**
    
    -   Run `python manage.py makemigrations` and `python manage.py migrate` to apply the database changes.
4.  **Admin Access:**
    
    -   Create a superuser account using `python manage.py createsuperuser`.
    -   Access the admin panel at `/admin/` and log in with the superuser credentials.
## Using the Admin Interface

The heart of the project lies in the Django admin interface, where you can manage products, customers, payments, and financial status. Follow these steps to get started:

1.  **Customers:**
    
    -   Add new customers with their names and phone numbers.
    -   Customer check IDs are automatically generated.
2.  **Product Purchases:**
    
    -   For each customer, add product purchases.
    -   Provide product details such as name, cost, tax rate, and starting fee.
    -   Set payment-related details like next payment amount, duration, and status.
3.  **Payments and Financial Status:**
    
    -   Record payments made by customers under each product purchase.
    -   The financial status of each purchase is automatically updated based on payments.
## Automations and Calculations

The Auto Nasiya project automates several tasks for your convenience:

-   **Auto Field Calculations:**
    
    -   Total price, duration, and next payment amount are automatically calculated based on provided data.
-   **Financial Tracking:**
    
    -   The project tracks payments and maintains the financial status of each product purchase.

## Customizing and Extending

The project structure allows for easy customization and extension:

-   **Signals:**
    
    -   Automatic calculations and updates are triggered using Django signals.
    -   Modify signal functions in `authapp/signals.py` and `core/signals.py` as needed.
-   **Utilities:**
    
    -   Custom utility classes are available in `authapp/utils.py` and `core/utils.py`.
    -   Adjust calculations or add new functionality by modifying these classes
    
## Conclusion

The Auto Nasiya project simplifies Nasiya product management through automation and efficient tracking. Leverage the Django admin interface and automated calculations to streamline your tasks and ensure accurate financial tracking.

For more detailed information, refer to the project's codebase and comments in individual files.
