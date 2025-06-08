# 🩺 Healthcare Backend API

A secure and scalable healthcare backend system built with Django REST Framework, PostgreSQL, and JWT authentication. This API allows authenticated users to manage patients, doctors, and patient–doctor mappings.

---

## 🚀 Live Deployment

- 🔗 **Render App**: https://healthcare-backend-alde.onrender.com/

- 📬 **Testing Guide**: [test_guide.html](https://healthcare-backend-alde.onrender.com/api/test-guide)
  
- 📬 **Postman Testing Workspace**: <br>
          - [Workspace Link with local url](https://www.postman.com/test55-1090/workspace/healthcare-backend-local-url)  <br>
          - [Workspace Link with deployed url](https://www.postman.com/test55-1090/workspace/healthcare-backend-deployed-url)

- 📷 **Watch The Demo**: [YouTube video link](https://youtu.be/w_KbNu_XBqs)

---

## 🎯 Features

- ✅ User Registration & JWT Login
- ✅ Create, Read, Update, Delete Patients and Doctors
- ✅ Assign Doctors to Patients
- ✅ Permissions & Owner-based access
- ✅ Validations & error handling
- ✅ Ready for deployment (Render/Heroku)

---

## 🛠️ Tech Stack

| Component      | Stack                               |
| -------------- | ----------------------------------- |
| Backend        | Django, Django REST Framework       |
| Authentication | JWT (djangorestframework-simplejwt) |
| Database       | PostgreSQL by Render                |
| Hosting        | Render                              |
| Docs UI        | HTML + JavaScript                   |
| Dev Tools      | Postman, VSCode, Git                |

---

## 📁 API Endpoints

### 🔐 Auth

| Method | Endpoint              | Description        |
| ------ | --------------------- | ------------------ |
| POST   | `/api/auth/register/` | Register user      |
| POST   | `/api/auth/login/`    | Login, returns JWT |
| GET    | `/api/auth/user/`     | Get current user   |

### 👤 Patients

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/patients/`      | Create patient       |
| GET    | `/api/patients/`      | List user’s patients |
| GET    | `/api/patients/<id>/` | Retrieve patient     |
| PUT    | `/api/patients/<id>/` | Update patient       |
| DELETE | `/api/patients/<id>/` | Delete patient       |

### 🧑‍⚕️ Doctors

| Method | Endpoint             | Description      |
| ------ | -------------------- | ---------------- |
| POST   | `/api/doctors/`      | Create doctor    |
| GET    | `/api/doctors/`      | List all doctors |
| GET    | `/api/doctors/<id>/` | Get doctor by ID |
| PUT    | `/api/doctors/<id>/` | Update doctor    |
| DELETE | `/api/doctors/<id>/` | Delete doctor    |

### 🔗 Mappings

| Method | Endpoint                      | Description                    |
| ------ | ----------------------------- | ------------------------------ |
| POST   | `/api/mappings/`              | Assign doctor to patient       |
| GET    | `/api/mappings/`              | List all mappings              |
| GET    | `/api/mappings/<patient_id>/` | Get patient’s assigned doctors |
| DELETE | `/api/mappings/delete/<id>/`  | Remove patient-doctor mapping  |

---

## 📦 Models & Fields

### 🔐 1. `User` Model (Custom)

Extends Django’s `AbstractUser` to use email as the login field.

```bash
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
```

| Field      | Type       | Description             |
| ---------- | ---------- | ----------------------- |
| `email`    | EmailField | Unique, used for login  |
| `username` | CharField  | Required by Django      |
| `password` | CharField  | Hashed, stored securely |

### 🤵🏼 2. `Patient` Model (Custom)

```bash
class Patient(models.Model):
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
```

| Field        | Type         | Description                  |
| ------------ | ------------ | ---------------------------- |
| `name`       | CharField    | Full name                    |
| `age`        | IntegerField | Age of the patient           |
| `gender`     | CharField    | Choices: `'M'`, `'F'`, `'O'` |
| `address`    | TextField    | Full address                 |
| `created_by` | ForeignKey   | User who created the patient |

### 🧑🏼‍⚕️ 3. `Doctor` Model (Custom)

```bash
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()
    contact = models.CharField(max_length=100)
```

| Field            | Type         | Description                |
| ---------------- | ------------ | -------------------------- |
| `name`           | CharField    | Doctor's full name         |
| `specialization` | CharField    | Field of medical expertise |
| `experience`     | IntegerField | Years of experience        |
| `contact`        | CharField    | Phone or email             |

### 🔗 4. `PatientDoctorMapping` Model (Custom)

```bash
class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
```

| Field     | Type       | Description       |
| --------- | ---------- | ----------------- |
| `patient` | ForeignKey | Link to a patient |
| `doctor`  | ForeignKey | Link to a doctor  |

---

## ⚙️ Setup Instructions (Local)

### 1. Clone Project

```bash
git clone https://github.com/YashBaraii/Healthcare_Backend.git
cd Healthcare_Backend
```

2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On MacOS: source venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Set up .env <br>
   Create .env:

```bash
# Mandatory
SECRET_KEY=
DEBUG=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

# OR

DATABASE_URL=postgresql://<user>:<pass>@localhost:5432/db_name
```

6. Run Migrations

```bash
python .\manage.py makemigrations
python .\manage.py migrate
```

7. Create Superuser (optional)

```bash
python .\manage.py createsuperuser
```

8. Run Server

```bash
python .\manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## 🧪 Testing

- 🧠 Test JWT-protected APIs using **Postman** or **Thunder Client**
- Postman testing workspace link: [Workspace](https://www.postman.com/test55-1090/workspace/healthcare-backend-local-url). For testing APIs locally.
- Include `Authorization: Bearer <access_token>` header
- Use [`test_guide.html`](https://healthcare-backend-alde.onrender.com/api/test_guide.html) to copy test payloads
- You can also test in browser with session login (`SessionAuthentication` – dev only)

---

🧑‍💻 Contributors
Yash Barai [(@YashBaraii)](https://github.com/YashBaraii)

<br>

📜 License
This project is licensed under the [MIT](https://github.com/YashBaraii/Healthcare_Backend/blob/main/LICENSE) License.

<br>

📬 Contact
For questions or feedback, connect via LinkedIn or raise an issue on the repository.
