from django.shortcuts import render


def home(request):
    projects = [
        {
            "image": "project1.jpg",
            "title": "Infrastructure Monitoring",
            "description": "Built a cloud dashboard using Azure Monitor and Grafana for real-time analytics and alerting."
        },
        {
            "image": "project2.jpg",
            "title": "Automation Toolkit",
            "description": "Python and PowerShell scripts for server health checks, backups, and task automation."
        },
        {
            "image": "project3.jpg",
            "title": "Cloud Provisioning",
            "description": "Automated VM creation and configuration using Terraform and Azure CLI."
        },
        {
            "image": "project4.jpg",
            "title": "CI/CD Pipeline",
            "description": "Configured GitHub Actions for automated testing, build, and deployment of Django apps."
        }
    ]
    return render(request, 'portfolio/home.html', {"projects": projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def projects(request):
    return render(request, 'portfolio/projects.html')
