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

### **Task 3:** allure report app support (commited: 040124)
1. Implement 3 endpoints  of your API
   - Folders
   - Lists
   - Spaces
2. Reports in allure should be included
3. At least 2 functional tests should be included
   - Test that a folder with the same name cannot create
   - Test Space with this name already exists
   - Test Space not found
   - Test empty json input returns 400 error [List, Folder, Space]
#### Others things on the commits:
- Fix some issues found by pylint app
- Added response validation.
- Enhanced Spaces and Folders test cases.
- Updated and Enhanced rest_client.py and validate_response.py files.
- Added JSON files for validation.
- Included JSON payload for API requests.
- Improved rest_client and configuration.
- ![img.png](Docs/img.png)