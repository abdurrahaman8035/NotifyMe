# Notify Me

Notify Me is a Django app that enables instructors to send messages to students using SMS for convenience. The app provides features such as managing contacts, composing and sending SMS messages.

## Features

- Contact Management: Instructors can add, edit, and delete contacts associated with their classes or courses.
- SMS Messaging: Instructors can compose and send SMS messages to individual contacts or groups of contacts.
- Convenience: The app allows instructors to conveniently communicate with students via SMS, reducing the need for other communication channels.

## Requirements

- Python 3.x
- Django 3.x
- Twilio (for sending SMS)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/abdurrahaman8035/NotifyMe.git
   ```

2. Navigate to the project directory:

   ```bash
   cd NotifyMe
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure Twilio credentials:

   - Rename the `example.env` file to `.env`.
   - Open the `.env` file and update the values for `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN` with your Twilio account credentials.

6. Run database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your browser and visit `http://localhost:8000` to access the app.

## Usage

1. Register as an instructor or log in if you already have an account.
2. Add contacts by providing the necessary details such as name, phone number, and any additional information.
3. Compose an SMS message, selecting the desired contacts or groups of contacts as recipients.
4. Send the SMS message, and it will be delivered to the specified contacts' phone numbers.

## Contributing

Contributions are welcome! If you encounter any bugs, have suggestions, or would like to add new features, please open an issue or submit a pull request.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Acknowledgments

This project was inspired by the need for a simple SMS-based communication tool for instructors and students.
