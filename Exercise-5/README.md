# Exercise 5: Docker Security with AppArmor Profiles

## Objective
Harden Docker container security by defining and enforcing custom **AppArmor Mandatory Access Control (MAC)** profiles. This prevents container escape vulnerabilities, limits access to sensitive host and system directories (e.g. `/etc/shadow`, `/proc/sys/kernel`), and restricts unauthorized executable execution.

## Scenario
Deploying a Python web application in high-compliance production environments. An AppArmor profile (`docker-profile-secure`) mediates container system calls and file access, ensuring least privilege principles even if the container is compromised.

## Files Included
- `app.py`: Hardened Flask web service
- `Dockerfile`: Container image specification
- `docker-profile-secure`: Custom AppArmor MAC security profile
- `test_security.py`: Python validation script testing restricted vs allowed capabilities
- `screenshots/`: Execution proof captures

## Execution Steps
1. **Define Security Profile (`docker-profile-secure`)**:
   Explicitly deny read/write to `/etc/shadow*`, `/proc/sys/kernel/**`, and kernel tuning parameters.
2. **Parse and Load Profile into Kernel**:
   ```bash
   sudo apparmor_parser -r -W docker-profile-secure
   ```
3. **Build the Flask Image**:
   ```bash
   docker build -t flask-apparmor .
   ```
4. **Run Container with Security Profile Enforcement**:
   ```bash
   docker run -d --name secure-flask --security-opt "apparmor=docker-profile-secure" -p 5000:5000 flask-apparmor
   ```
5. **Execute Security Verification Script**:
   ```bash
   docker exec -it secure-flask python test_security.py
   ```

## Execution Proof (Screenshots)
- `screenshots/01-apparmor-profile-definition.png`: Profile definition and syntax validation
- `screenshots/02-docker-build-security-image.png`: Docker image build log
- `screenshots/03-enforce-apparmor-profile.png`: Container launch with `--security-opt`
- `screenshots/04-restricted-access-prevention-test.png`: Security test output proving permission denial on protected resources
