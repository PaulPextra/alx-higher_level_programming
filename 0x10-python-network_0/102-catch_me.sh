#!/bin/bash
# Get request to the URL and display the body of the response
curl -sLX PUT -d "You got me!" -H "Origin: X-School-User-Id" 0.0.0.0:5000/catch_me
