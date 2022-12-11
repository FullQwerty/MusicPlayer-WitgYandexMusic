style = """
.QPushButton {
    text-decoration: none;
    display: inline-block;
    color: black;
    padding: 10px 15px;
    margin: 5px 10px;
    border:2px solid #000000;
    border-radius: 6px 6px 6px 6px;
    -webkit-border-radius: 6px 6px 6px 6px;
    -moz-border-radius: 6px 6px 6px 6px;
    font-family: 'Verdana', sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    background-image: linear-gradient(to right, #9EEFE1 0%, #4830F0 51%, #9EEFE1 100%);
    background-size: 200% auto;
    box-shadow: 0 0 20px rgba(0, 0, 0, .1);
    transition: .5s;
} 
.QPushButton:hover {
    background-color: #ffa500; /* Green */
    color: black; 
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);}

 """

slider_style = """
QSlider::groove:horizontal  {
    border: 1px #ffffff;
    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #ffffff);
    margin: 2px  0;
}

QSlider::handle:horizontal  {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop: 0 #ffa500, stop:1 #ffa500);
    border: 1px solid #ffa500;
    width: 18px;
    margin: -2px  0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
    border: 3px;
}
"""