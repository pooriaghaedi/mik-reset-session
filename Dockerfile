from python:3

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV ADIP="Active Directory IP address"
ENV ADDomain="site1"
ENV MikIP="Mikrotik IP Adress"
ENV MikUsername="admin"
ENV MikPassword="password"

EXPOSE 5000
CMD ["python", "./run.py"]
