# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut, yang telah berdiri sejak tahun 2000, dikenal sebagai institusi pendidikan berkualitas tinggi dengan banyak lulusan sukses. Namun, institusi ini menghadapi tantangan besar dengan tingkat dropout siswa yang tinggi, yang dapat merusak reputasi dan keberlanjutan operasionalnya. Untuk mengatasi masalah ini, Jaya Jaya Institut berupaya mendeteksi siswa yang berpotensi dropout lebih dini sehingga dapat diberikan intervensi dan bimbingan khusus. 
Dengan memanfaatkan analisis data dan model prediksi, institusi dapat mengidentifikasi faktor-faktor risiko yang menyebabkan dropout. Selanjutnya, melalui pengembangan dashboard interaktif, institusi dapat memantau performa siswa secara real-time, memungkinkan pengambilan keputusan berbasis data yang lebih baik dan intervensi tepat waktu. Tujuan akhir dari upaya ini adalah untuk mengurangi tingkat dropout, meningkatkan retensi siswa, dan memperkuat reputasi Jaya Jaya Institut sebagai lembaga pendidikan terkemuka.

### Permasalahan Bisnis
Permasalahan bisnis yang dihadapi Jaya Jaya Institut adalah tingginya tingkat siswa yang tidak menyelesaikan pendidikan alias dropout. Hal ini berdampak negatif pada reputasi institusi, kepuasan siswa, serta keberlanjutan operasional dan finansial. Tingkat dropout yang tinggi mencerminkan adanya masalah dalam manajemen siswa, dukungan akademik, dan bimbingan yang diberikan, yang pada akhirnya mengurangi jumlah lulusan yang berhasil dan mempengaruhi citra institusi secara keseluruhan.

### Cakupan Proyek
- Melakukan cleansing data pada data target dengan keterangan "Enrolled"
- Melakukan analisis dan penggalian informasi mengenai `Status` dari dataset yang disediakan
- Melakukan exploratory data analysis dan memilih feature important yang berpengaruh terhadap `Status Performance dari Students`
- Membuat model machine learing untuk memprediksi apakah student tersebut Dropout atau tidak. Model yang digunakan adalah CatBoost Classifier
- Menguji model yang telah dilatih menggunakan data dummy yang di input langsung
- Membuat dashboard dari analisis yang sudah dikerjakan

### Persiapan

Sumber data: https://raw.githubusercontent.com/rhisadkaptri/Dicoding/main/data.csv

#### Setup environment:
1. Buka Folder submission di Visual Studio Code
2. Buka terminal di VSCode dengan menekan Ctrl + Backtick (biasanya tombol di sebelah kiri tombol 1).
Di terminal, Anda dapat membuat virtual environment (venv) menggunakan perintah berikut:
```
python -m venv env
```
3. Setelah itu aktifkan Virtual Environment. Aktifkan virtual environment yang telah diberikan.
   Pada Windows:
```
.\env\Scripts\activate
```
   Pada macOS dan Linux:
```
source env/bin/activate
```
4. Instal Paket dari requirements.txt
Di terminal Visual Studio Code, instal semua paket yang terdaftar dalam file requirements.txt. Perintah ini akan menginstal semua paket Python yang diperlukan beserta versi yang sesuai ke dalam environment.dengan menggunakan pip:
```
pip install -r requirements.txt
```
5. Verifikasi Instalasi
Setelah proses instalasi selesai, pastikan semua paket yang terdaftar di requirements.txt telah terinstal dengan benar. Ini untuk melihat daftar paket yang terinstal berserta versinya, dengan menjalankan:
```
pip list
```
6. Selesai

## Business Dashboard
Dashboard yang saya buat berisikan analisis mengenai `Student Status Performance`

![Dashboard](https://github.com/rhisadkaptri/Dicoding2/assets/76622802/92efd359-9cca-4508-b19b-b3ea2e9f7b00)
Link Dashboard: https://public.tableau.com/views/DashboardStudentStatus/Dashboard1?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link


## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Berdasarkan analisis yang telah dilakukan, feature yang paling berpengaruh adalah:
1. `Curricular_units` merupakan feature yang sangat berpengaruh terhadap `Status Student Performance`, disini saya mengelompokkannya menjadi 3, yaitu:
   - `Curricular_units_Grade`: Jika dibandingkan Curricular units antara semester 1 dan 2. Jika `Curricular_units` di semester 2 lebih rendah dari `Curricular_units` di semester 1, ada kemungkinan dia akan Dropout, dan sebaliknya.
   - `Curricular_units_Approved`: Jika dibandingkan Curricular units antara semester 1 dan 2. Jika `Curricular_units` di semester 2 lebih rendah dari `Curricular_units` di semester 1, ada kemungkinan dia akan Dropout, dan sebaliknya.
   - `Curricular_units_Evaluation`: Jika dibandingkan Curricular units antara semester 1 dan 2. Jika `Curricular_units` di semester 2 lebih tinggi dari `Curricular_units` di semester 1, ada kemungkinan dia akan Dropout, dan sebaliknya.
2. `Tuition_fees_up_to_date` merupakan feature yang berpengaruh selanjutnya terhadap `Status Student Performance`, ternyata jika dibandingkan anatara `Tuition_fees_up_to_date` yang berstatus `Yes` dan `No`, lebih banyak student yang berstatus Yes. Akan tetapi, student yang berstatus `No` lebih banyak yang dropout daripada yang graduated padahal jumlahnya lebih sedikit daripada student yang berstatus `Yes` lebih banyak yang graduated daripada yang dropout.
3. `Scholarship_holder` merupakan feature yang juga berpengaruh terhadap Status Student Performance, student yang tidak mendapat beasiswa, memiliki selisih perbandingan yang tidak jauh antara yang graduated dan dropout. Jika dibandingkan dengan student yang mendapat beasiswa, memiliki selisih perbandingan yang lumayan jauh antara student yang graduated daripada yang dropout.

### Rekomendasi Action Items (Optional)

Beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka menurut saya dari analisis tersebut adalah:
- Curricular_units (Grade, Approved, Evaluation): Lakukan pemantauan berkelanjutan terhadap performa akademik siswa di setiap semester dengan menciptakan sistem peringatan dini bagi siswa yang mengalami penurunan nilai atau evaluasi. Berikan bimbingan tambahan, sesi tutoring, atau kelas remedial untuk siswa yang menunjukkan penurunan dalam kinerja akademik mereka. Tinjau dan revisi kurikulum untuk memastikan bahwa materi yang disampaikan relevan dan dapat dipahami dengan baik oleh siswa, terutama di semester yang menunjukkan penurunan kinerja.
- Tuition_fees_up_to_date: Identifikasi siswa yang mengalami kesulitan dalam membayar biaya pendidikan dan tawarkan bantuan keuangan atau opsi pembayaran yang fleksibel. Kembangkan program pembiayaan atau skema pembayaran yang lebih terjangkau untuk membantu siswa mengelola pembayaran biaya pendidikan mereka. Edukasi siswa dan orang tua mengenai pentingnya pembayaran tepat waktu dan dampaknya terhadap kinerja akademik siswa.
- Scholarship_holder: Tingkatkan jumlah dan cakupan beasiswa yang ditawarkan untuk membantu lebih banyak siswa mengakses pendidikan tanpa beban finansial yang berat. Revisi kriteria penerimaan beasiswa untuk menjangkau lebih banyak siswa yang berpotensi dropout karena masalah finansial. Berikan pendampingan dan mentoring khusus untuk penerima beasiswa agar mereka dapat memaksimalkan potensi akademik mereka dan mengurangi kemungkinan dropout.
