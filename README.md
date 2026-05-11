# Grocery Store Application

## Overview
The Grocery Store Application is a web-based platform built using Streamlit that allows users to manage grocery orders and inventory efficiently. The application features user authentication, order management, inventory tracking, and an AI assistant powered by OpenAI to assist users with their queries.

## Features
- **User Authentication**: Users can register, log in, and log out. The application supports role-based access for users and employees.
- **Order Management**: Users can create new orders, view active orders, and cancel existing orders.
- **Inventory Management**: Employees can view and manage inventory items, including adding new items and updating stock levels.
- **AI Assistant**: An integrated chatbot powered by OpenAI provides assistance and answers user queries.

## Project Structure
```
grocery-store-app
├── src
│   ├── app.py                # Main entry point of the application
│   ├── components
│   │   ├── auth.py           # User authentication functionalities
│   │   ├── inventory.py       # Inventory management features
│   │   ├── orders.py          # Order management functionalities
│   │   └── chatbot.py         # AI assistant integration
│   ├── utils
│   │   ├── file_handler.py     # Utility functions for file operations
│   │   └── helpers.py          # Helper functions for various tasks
│   └── models
│       ├── user.py            # User model and related methods
│       ├── order.py           # Order model and related methods
│       └── inventory_item.py   # Inventory item model and methods
├── requirements.txt           # Project dependencies
├── .env                       # Environment variables
└── README.md                  # Project documentation
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd grocery-store-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage
1. Run the application:
   ```
   streamlit run src/app.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. Follow the on-screen instructions to register or log in, manage orders, and interact with the AI assistant.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.