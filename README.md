# Django Wallet Application

## Overview
This is a Django-based wallet application that allows users to register, load money into their accounts, and transfer money to other users securely. The application ensures user authentication and tracks all financial transactions with timestamps.

## Distinctiveness and Complexity
This project stands out because of the following reasons:
- **User Authentication and Management:** Uses Django’s built-in authentication system to handle user login, registration, and session management.
- **Transactional System:** Implements a financial transaction system with logging, ensuring accurate debits and credits.
- **Security Measures:** Ensures that only authenticated users can perform transactions, prevents unauthorized balance modifications, and provides error handling for incorrect transactions.
- **Time Localization:** Includes Nepali DateTime conversion for transaction history, demonstrating an advanced feature of localizing timestamps.
- **Database Management:** Uses Django models to maintain wallet balances and transaction histories with efficient database queries.
- **Form Handling for Data Integrity:** Implements Django forms to ensure user input validation and prevent invalid transactions. Forms play a crucial role in maintaining data integrity, enforcing minimum transaction limits, and securing financial operations. The use of Django’s form validation system adds robustness to the project.

## File Descriptions
### `models.py`
- Has two models: `Client` (representing a user’s wallet) and `Transaction` (representing financial transactions).
- Implements methods for handling transaction timestamps with Nepali Standard Time (NST).

### `views.py`
- Contains view functions for core functionalities:
  - `dashboard()`: Displays wallet balance and recent transactions.
  - `load_money()`: Allows users to add money to their wallet.
  - `transfer_money()`: Facilitates money transfers between users.
  - `register()`: Handles user registration and account creation. Handles server-side validation of registration data
  - `custom_logout()`: Logs out users.

### `urls.py`
- Maps URL paths to their respective views:
  - `/` → Dashboard
  - `/register/` → User Registration
  - `/load/` → Load Money
  - `/transfer/` → Transfer Money
  - `/logout/` → Logout

### `forms.py`
- **`RegistrationForm`**: Extends Django's `UserCreationForm` to include `username`, `email`, `password1`, and `password2` fields for user registration.
- **`LoadMoneyForm`**: A simple form with an `amount` field that ensures users enter a valid decimal number greater than or equal to 1.00 when loading money.
- **`TransferMoneyForm`**: Contains fields for specifying a recipient’s username and a transfer amount, ensuring a minimum transfer of 1.00.

### `register_validations.js'
- Handles client-side validation. Error messages are displayed when fields are invalid and disappear as soon as the user starts typing.
- If the user tries to submit the form with missing or invalid information, error messages will appear:
- **Username is required** if the field is left empty.
- **Valid email is required** if the email field is empty or doesn't contain a valid `@` symbol
- **Valid Password is required** if the password is empty or password confirmation doesn't macth the password
- **Real-Time Error Removal**: As soon as the user starts typing in the `username` or `email` or `password` field, the corresponding error message disappears. This ensures that the user has an improved experience while filling out the form.
- **Form Submission Prevention**: The form is prevented from submitting if the validation fails, ensuring only valid data is submitted.

### `script.js`
**Toggle "See More" Button for Transactions**
This script controls the visibility of older transactions on the page. Initially, older transactions are hidden. When the "See More" button is clicked, the hidden transactions are revealed, and the button text changes to "See Less." Clicking it again hides the transactions and restores the "See More" text.

**How It Works**:
- On page load, the `seeMoreBtn` toggles the display of the `olderTransactions` div.
- The button text switches between "See More" and "See Less" based on the visibility of the transactions.

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Virtual environment (recommended)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd django-wallet-app
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   If `pytz` and `nepali_datetime` are not included in `requirements.txt`, install them manually:
   ```sh
   pip install pytz nepali-datetime
   ```
   Then, add them to `requirements.txt` by running:
   ```sh
   pip freeze > requirements.txt
   ```
4. Apply database migrations:
   ```sh
   python manage.py makemigrations wallet
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```
7. Open the browser and go to `http://127.0.0.1:8000/`.

## Additional Information
- Ensure that `requirements.txt` includes necessary dependencies such as Django, pytz, and nepali_datetime.
- Future enhancements could include integrating a third-party payment API or adding a mobile-friendly UI.

## License
This project is licensed under the MIT License.

