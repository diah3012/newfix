import streamlit as st

st.snow()

def main():
    st.title("Welcome")
    if st.button("~~Thi my profil~~"):
        st.write('this is my biography')
        st.image("foto.PNG")
    
    st.title("**DIAH RAHMA PERTIWI**")
    st.write("_Saya adalah seorang programmer yang memiliki minat dalam pengembangan web dan data science dalam bidang kesehatan.Saat ini programmer dalam bidang kesehatan masih jarang dan sangat dibutuhkan di Indonesia.Sebagai seorang programer, Saya telah terlibat dalam pengembangan aplikasi dan sistem yang mengoptimalkan layanan kesehatan. saya juga berkontribusi dalam pengembangan aplikasi mobile yang memungkinkan pasien untuk memantau kondisi kesehatan mereka, memperoleh informasi medis yang relevan, dan menghubungkan dengan tenaga medis secara virtual_")

    st.markdown("---")
    
    st.header("Profil")
    st.subheader("**Nama Lengkap:**")
    nama = st.text_input("", "Diah Rahma Pertiwi")

    st.subheader("**Tempat,Tanggal Lahir:**")
    ttl = st.text_input("", "Semarang, 30 Desember 2002")
    
    st.subheader("**Alamat:**")
    alamat = st.text_input("", "Jl.Mulawarman Selatan Raya RT.05/RW 02,Semarang")
    
    st.subheader("**Telephon:**")
    telepon = st.text_input("", "088706608293")
   
    st.subheader("**email:**")
    email = st.text_input("Email", "diahrhmp@gmail.com")
    
    # Pendidikan
    st.header("Pendidikan")
    st.write("- SMP N 27 Semarang")
    st.write("- SMA N 9 Semarang")
    st.write("- S1 Manajemen Informasi Kesehatan,Universitas Nasional Karangturi")

    # Pengalaman Kerja
    st.header("Pengalaman Kerja")
    st.write("- Magang di PT.Healthcare")
    st.write("  - Terlibat dalam pengembangan aplikasi web untuk manajemen dan analisis data klinis")
    st.write("  - Membantu dalam implementasi kecerdasan buatan untuk mendukung pengambilan keputusan klinis")
    st.write("  - Berkontribusi dalam pengujian dan pemeliharaan sistem aplikasi yang ada")

    # Skill
    st.header("**Skill**")
    skills = st.text_area("","Python, HTML, CSS, JavaScript, Data Analysis")
    st.write("Skill yang dikuasai: ", skills)

if __name__ == "__main__":
    main()
