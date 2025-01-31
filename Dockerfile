# Use an official Python runtime as a parent image
FROM python:3.10.9-slim

# Set the working directory in the container
WORKDIR /wine_quality_analysis

# Copy the current directory contents into the container at /wine_quality_analysis
COPY . /wine_quality_analysis

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "script/main.py"]
