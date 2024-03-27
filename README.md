## Historic:
### **Task 1:** about the cURL tool (commited: 030324)
### **Task 2:** Added basic CRUD for the Clickup application 'folder' API using the pytest module. (commited: 031724)
``` 
Requirements:
The .env file must contain the following kyes:
 - TOKEN=<A token generated for the 'clickup' app>
 - SPACE_ID=<a space ID created>
``` 
#### CRUD functionality
   - Authentication
   - Create folder
   - Read folder
   - Update folder
   - Delete folder
   - Cleanup
#### Additional functionality:
- Get all folders

**Task 3:** allure report app support (commited: 032724)
- Fix some issues found by pylint app
- Added response validation.
- Included test cases for the 'List' endpoint.
- Included test cases for the 'Sp[aces' endpoint.
- Enhanced Spaces and Folders test cases.
- Updated rest_client.py and validate_response.py files.
- Added JSON files for validation.
- Included JSON payload for API requests.
- Implemented functional tests.
- Improved rest_client and configuration.
- Enhanced conftest.py and validate_response.py files.
- Added support for Allure report app.