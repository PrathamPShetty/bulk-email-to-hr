from dotenv import load_dotenv
import os

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")
filename = os.getenv("FILENAME", "resume.pdf")


subject = "Seeking Opportunity for Developer Role – Pratham P Shetty"

body = """
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; font-size: 15px; color: #333;">

<p>I am reaching out to express my interest in an opportunity as a Developer at your organization. 
I specialize in <b>Artificial Intelligence</b> and <b>Full-Stack Development</b> and have hands-on 
experience in building scalable, production-ready applications using modern technologies.</p>

<p>I have worked extensively with <b>Python</b>, <b>JavaScript</b>, <b>TypeScript</b>, 
<b>Django</b>, <b>FastAPI</b>, <b>Express.js</b>, and <b>Nest.js</b> to develop secure and 
high-performance backend systems. On the frontend, I build responsive and user-friendly interfaces using 
<b>React</b>, <b>Next.js</b>, <b>Tailwind CSS</b>, and <b>Flutter</b>. I also have practical 
experience in cloud deployment and DevOps using <b>Docker</b>, <b>Nginx</b>, and <b>Azure VPS</b>.</p>

<p>In addition to full-stack development, I actively work on AI and LLM-based systems using 
<b>RAG</b>, <b>LangChain</b>, and <b>LangGraph</b>, integrating contextual AI workflows into 
real-world applications.</p>

<p>I am passionate about writing clean, maintainable code and building efficient systems that 
solve real-world problems. My resume is attached.</p>

<p>Thank you for your time and consideration. I look forward to your response.</p>

</body>
</html>
"""



