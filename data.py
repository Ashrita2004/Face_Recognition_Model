import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://faceattendancesystem-1cf6e-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
   "7003" : {
        "name" : "Abhinil Savarni",
        "Roll No" : 220710007003,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },    
"7004" : {
        "name" : "Abhishek Prasad",
        "Roll No" : 220710007004,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },   
"7005" : {
        "name" : "Abhishek saikia",
        "Roll No" : 220710007005,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7006" : {
        "name" : "Agniraj kashyap dutta",
        "Roll No" : 220710007006,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7009" : {
        "name" : "Aakash Sarmah",
        "Roll No" : 220710007009,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7010" : {
        "name" : "Akhrang Boro",
        "Roll No" : 220710007010,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7011" : {
        "name" : "Anwesha Changkakoty",
        "Roll No" : 220710007011,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7014" : {
        "name" : "Ashish saikia",
        "Roll No" : 220710007014,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7015" : {
        "name" : "Ashrita Lahon",
        "Roll No" : 220710007015,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7016" : {
        "name" : "Atrayee Phukan",
        "Roll No" : 220710007016,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7018" : {
        "name" : "Bhikrant Borah",
        "Roll No" : 220710007018,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7020" : {
        "name" : "Bishal Ranjan Nath",
        "Roll No" : 220710007020,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },    
"7022" : {
        "name" : "Debasish Rabha",
        "Roll No" : 220710007022,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7023" : {
        "name" : "Debraj Dutta",
        "Roll No" : 220710007023,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },    
"7025" : {
        "name" : "Dorothy Gogoi",
        "Roll No" : 220710007025,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7027" : {
        "name" : "Iffat Ahad Jahan",
        "Roll No" : 220710007027,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7028" : {
        "name" : "Ishan Bhardwaj",
        "Roll No" : 220710007028,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7029" : {
        "name" : "Ishani gogoi",
        "Roll No" : 220710007029,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7030" : {
        "name" : "Lakhya Jyoti Saikia",
        "Roll No" : 220710007030,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7034" : {
        "name" : "Mayurakhya Nath",
        "Roll No" : 220710007034,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7037" : {
        "name" : "Nabadeep dutta",
        "Roll No" : 220710007037,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7038" : {
        "name" : "Nabajyoti Das",
        "Roll No" : 220710007038,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7039" : {
        "name" : "Niharanjan Gohain",
        "Roll No" : 220710007039,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7042" : {
        "name" : "Nitul Das",
        "Roll No" : 220710007042,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7047" : {
        "name" : "Rakib Hussain",
        "Roll No" : 220710007047,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },            
"7050" : {
        "name" : "Sameer Jyoi Kashyap",
        "Roll No" : 220710007050,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7051" : {
        "name" : "Sampriti Kalita",
        "Roll No" : 220710007051,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7054" : {
        "name" : "Shaswata Gogoi",
        "Roll No" : 220710007054,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7055" : {
        "name" : "Sourav Kumar Barman",
        "Roll No" : 220710007055,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },    
"7056" : {
        "name" : "Suvan Sinha",
        "Roll No" : 220710007056,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },
"7061" : {
        "name" : "Vishal Kr Sharma",
        "Roll No" : 220710007061,
        "total_attendance" : 0,
        "last_attendance_time" : "03-10-2024 00:54:34",
        "Starting year" : "2022"
    },

}
for key,value in data.items():
    ref.child(key).set(value)