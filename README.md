# **Med Plus Application**

## **Overview**

The Medication Reminder Application is designed to help users, caregivers, and children manage medication schedules efficiently. The application offers user login functionality with role-based access for users, caregivers, and children. The app provides a comprehensive platform to track medications, set reminders, and store prescription details using QR code integration.

## **Features**

### **1. User Authentication and Role Management**
- **Three Types of Login:** Supports login for three types of users: 
  - **User**: The primary user of the application.
  - **Caregiver**: A user with access to manage medications for others.
  - **Child**: Limited access for children with parental or caregiver oversight.
- **JWT Authentication:** Ensures secure login and session management using JWT tokens.

### **2. Upcoming Medication Reminders**
- Displays an **upcoming medications list** based on scheduled reminders set by the user or caregiver.
- Tracks medications that need to be taken and sends reminders at appropriate times.

### **3. Medication Information**
- Users can view a detailed **medication information page** that displays:
  - Medication purpose
  - Dosage
  - Side effects
  - Precautions and warnings
- Integrated with a **QR code scanner** that retrieves medication information and adds it to the user’s profile.

### **4. Prescription Management**
- A **prescription page** that lists all medications added by the user.
- Provides instructions for each medication, including dosage and schedule.
- Users can add medications directly to their reminder list.

### **5. QR Code Integration**
- **QR code** support allows users to scan medication packaging and automatically import medication details into the system.
- The medication is then added to the user’s profile and reminder schedule.

### **6. Reminders Page**
- Displays medications added from QR codes or manually input, including:
  - Dosage
  - Time to take the medication
- Ensures the user is notified of upcoming doses at the right time.

### **7. Admin Role**
- **Caregivers** and **parents** can manage medications for their children.
- They can update schedules, edit medication details, and monitor medication adherence.

## **API Endpoints**

| **Endpoint**                   | **Description**                                          |
|---------------------------------|----------------------------------------------------------|
| `POST /auth/login`              | User login and JWT token generation.                     |
| `POST /auth/register`           | Register a new user (user, caregiver, child).            |
| `GET /medications`              | Fetch all medications for a user.                        |
| `POST /medications`             | Add a new medication to the user’s profile.              |
| `GET /medications/{id}`         | Get detailed information for a specific medication.      |
| `POST /qr/scan`                 | Scan QR code and add medication to user profile.         |
| `GET /reminders`                | List all medication reminders for the user.              |
| `POST /reminders`               | Create a reminder for a medication.                      |
| `PUT /users/{id}`               | Update user information.                                 |
| `DELETE /users/{id}`            | Delete a user.                                           |




