# IIS Core Concepts

### 1. Websites
- **Definition:** A website in IIS is a collection of web pages and associated resources that are served to users over the internet or an intranet.
- **Configuration:** Each website can have its own settings, including bindings (IP address, port, and hostname), physical path (location of files), and authentication methods.

### 2. Application Pools
- **Definition:** An application pool is a container for one or more websites or applications. It isolates them from other applications on the server.
- **Benefits:** This isolation helps manage resources and improves security; if one application crashes, it does not affect others.

### 3. Virtual Directories
- **Definition:** A virtual directory is a directory that is mapped to a physical directory on the server but does not correspond directly to a URL path.
- **Usage:** It allows administrators to organize content in a way that does not require moving files physically on the server.

## IIS Architecture

- **Request Processing:** IIS uses a request-processing architecture where HTTP.sys listens for incoming requests. When a request is received, it is processed by the Windows Process Activation Service (WAS), which manages application pools and worker processes (w3wp.exe).
- **Modules:** IIS supports various modules that can be added or removed to process requests (e.g., authentication modules, compression modules).
  
## IIS Security

### 1. Authentication
- **Types:**
  - **Anonymous Authentication:** Allows users to access the website without providing credentials.
  - **Windows Authentication:** Uses Windows credentials for user authentication.
  - **Basic and Digest Authentication:** Provide alternative methods for user validation.

### 2. Authorization
- **Role-Based Access Control (RBAC):** Administrators can set permissions based on user roles to restrict access to specific resources.

### 3. SSL/TLS
- **Encryption:** Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are used to encrypt data transmitted between the client and server.
- **Certificates:** SSL certificates must be installed on the server to enable HTTPS connections.

## IIS Configuration

### 1. Bindings
- **Definition:** Bindings define how a website responds to requests based on IP address, port number, and hostname.
- **Configuration Options:** Websites can be configured to listen on multiple bindings for different domains or IP addresses.

### 2. Application Settings
- **Configuration Options:** Settings include .NET CLR version, identity type for application pools, and custom error pages.

### 3. Logging
- **Log File Configuration:** IIS can log requests in various formats (W3C, NCSA). Logs can be configured to capture details such as client IP address, request URL, response status codes, etc.

## IIS Deployment and Management

### Deployment
- **Web Deploy Tool:** A powerful tool for deploying web applications from development environments to production servers.
- **IIS Manager:** The graphical interface used to manage IIS settings, websites, application pools, and security configurations.

### Management
- **Remote Management:** Administrators can manage IIS remotely using IIS Manager or PowerShell commands.
- **Monitoring Tools:** Tools like Performance Monitor and Event Viewer help track server performance and diagnose issues.

## Basic Troubleshooting

1. **Check Event Viewer:**
   - Review logs in Event Viewer for any errors related to IIS or specific applications.

2. **Inspect Log Files:**
   - Analyze IIS log files for unusual patterns or errors that may indicate issues with requests.

3. **Test Connectivity:**
   - Use tools like `ping` or `telnet` to check network connectivity to the server.

4. **Review Application Pool Status:**
   - Ensure that application pools are running and not in a stopped state due to errors.

5. **Use Failed Request Tracing:**
   - Enable tracing for detailed error analysis when requests fail.

By understanding these core concepts and best practices related to IIS, administrators can effectively deploy, manage, secure, and troubleshoot web applications hosted on Windows Server environments.

Citations:
[1] https://www.oneops.com/user/design/ms-iis-website-component.html
[2] https://platform.docs.cinchy.com/deployment-guide/deployment-guides/deployment-planning-overview-and-checklist/deployment-architecture-overview/iis-deployment-architecture
[3] https://vanseodesign.com/web-design/iis-web-server/
[4] https://www.techtarget.com/searchwindowsserver/definition/IIS
[5] https://www.geeksforgeeks.org/iis-full-form/