Simple Socket-Based Vlog Web App

This project is a minimal web application built from scratch using Python sockets without any web frameworks. It demonstrates how HTTP works at a low level while still supporting real-world features such as routing, forms, database interaction, and page navigation.

The app allows users to create, view, open in detail, and delete vlogs through a browser using a custom-built HTTP server.

Key Features

*   Custom HTTP server built using Python socket programming
    
*   Manual request parsing (method, path, headers, body)
    
*   HTML pages rendered dynamically without templates or frameworks
    
*   Create new vlog posts using HTML forms
    
*   List all vlogs on the home page
    
*   Open a vlog in a detailed view by clicking on it
    
*   Delete vlogs using POST requests
    
*   Redirect after POST actions (Post → Redirect → Get pattern)
    
*   Persistent storage using a database
    
*   Clean separation between routing, handlers, and database logic
    

Project Structure Overview

*   main.py: Entry point that starts the socket server
    
*   server.py: Handles socket connections and request lifecycle
    
*   router.py: Routes HTTP requests to appropriate handlers
    
*   handlers/: Contains request handlers (list, create, delete, detail, not found)
    
*   db/: Database manager and query functions
    
*   static/: HTML files (if any)
    
*   templates/: Dynamic HTML content (generated in code)
    

Technologies Used

*   Python 3
    
*   Socket programming
    
*   HTTP protocol (manual implementation)
    
*   HTML & basic CSS
    
*   SQL database (via custom DB manager)
    

Why This ProjectThis project was built for learning purposes to deeply understand:

*   How browsers communicate with servers
    
*   How HTTP requests and responses work internally
    
*   How routing, redirects, and form submissions work without frameworks
    
*   The importance of using database IDs instead of in-memory indexes
    
*   Proper backend patterns such as PRG (Post → Redirect → Get)
    

How It Works

1.  The server listens on a TCP socket
    
2.  Incoming HTTP requests are parsed manually
    
3.  Requests are routed based on method and path
    
4.  Handlers generate HTML responses
    
5.  Database operations persist data
    
6.  After POST actions, the server redirects to ensure fresh state
    

This project intentionally avoids frameworks like Flask or Django to focus on fundamentals.

Future Improvements

*   Edit vlog feature
    
*   Pagination
    
*   User authentication
    
*   Better styling and layout
    
*   REST-style URLs
    
*   Comments and likes
    
*   File uploads for video content
    

AuthorOllayorbek MasharipovSoftware Engineering studentBackend & systems programming enthusiast