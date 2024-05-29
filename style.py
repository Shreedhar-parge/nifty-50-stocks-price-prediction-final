import streamlit as st

# CSS styles
css_styles = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@200;300;400;500;600;700&display=swap');
* {
    padding: 0;
    margin: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
}
body {
    background: #e4e9f7;
    background-image: url('https://jupiter.money/blog/wp-content/uploads/2022/08/19.-Investment_strategies_for_beginners-1.jpg');
    background-size: cover;
}
.container {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 90vh;
}
.box {
    background: #fdfdfd;
    display: flex;
    flex-direction: column;
    padding: 25px 25px;
    border-radius: 20px;
    box-shadow: 0 0 128px 0 rgba(0, 0, 0, 0.1),
                0 32px 64px -48px rgba(0, 0, 0, 0.5);
    background-image: url('https://cdn1.vectorstock.com/i/1000x1000/27/00/symbol-stock-market-bull-and-bear-vector-26872700.jpg');    
    background-size: cover;      
}
.form-box {
    width: 450px;
    margin: 0px 10px;
}
.form-box header {
    font-size: 25px;
    font-weight: 600;
    padding-bottom: 10px;
    border-bottom: 1px solid #e6e6e6;
    margin-bottom: 10px;
}
.form-box form .field {
    display: flex;
    margin-bottom: 10px;
    flex-direction: column;
}
.form-box form .input input {
    height: 40px;
    width: 100%;
    font-size: 16px;
    padding: 0 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    outline: none;
}
.btn {
    height: 35px;
    background: rgba(76, 68, 182, 0.808);
    border: 0;
    border-radius: 5px;
    color: #fff;
    font-size: 15px;
    cursor: pointer;
    transition: all .3s;
    margin-top: 10px;
    padding: 0px 10px;
}
.btn:hover {
    opacity: 0.82;
}
.submit {
    width: 100%;
}
.links {
    margin-bottom: 15px;
}
</style>
"""

# Render CSS styles using st.markdown
st.markdown(css_styles, unsafe_allow_html=True)

# Display content in Streamlit
st.markdown("""
<div class="container">
    <div class="box form-box">
        <header>Login</header>
        <form>
            <div class="field input">
                <label for="email">Email</label>
                <input type="text" name="email" id="email" autocomplete="off" required>
            </div>
            
            <div class="field input">
                <label for="password">Password</label>
                <input type="password" name="password" id="password" autocomplete="off" required>
            </div>

            <div class="field">
                <button type="submit" class="btn">Login</button>
            </div>
            <div class="links">
                Don't have an account? <a href="register.php">Sign Up Now</a>
            </div>
           
        </form>
    </div>
</div>
""", unsafe_allow_html=True)
