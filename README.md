🔹 1. User Interface Layout 
Main Window:
Input fields: Drug Name, Target Name
Buttons: Search, Visual Interaction, Load CSV
Output: Result in a new window
🔹 2. System Modeling (Use Case Diagram)
Actors:
User : researcher ,student ,pharmacologist,doctor
Use Cases:
Load dataset
Search drug-target interaction
View result
Visualize network interaction

🔹 3. Activity Diagram
<img width="900" height="1167" alt="image" src="https://github.com/user-attachments/assets/ebf1de7d-a81c-49d4-a3a3-3ee9317e0c55" />

 


SDLC Phases for Drug-Target Interaction Prediction System
SDLC Phase	Status	Details / Description
1. Requirement Analysis	Completed	 identified the goal of the project: to input drug/target names and predict interactions.
2. System Design	Completed	Designed the UI layout, use case diagram, and activity diagram for user interactions.
3. Implementation (Coding)	 Not Started	Development will begin from 24 July, focusing on core features using Python + Tkinter.
4. Testing	Pending	After implementation, we will test various user inputs and edge cases.
5. Deployment	Pending	Final application will be deployed locally or shared via GitHub for demonstration.
6. Maintenance	Future	Will fix bugs and enhance the system based on user feedback after deployment.




 

Drug Target Prediction System

 1.Drug.py (Already provided above)
Contains the  GUI framework with placeholders and layout using Tkinter.

This is a GUI-based Python application that will allow users to:
- Load drug-target interaction datasets
- Search for interactions by drug or target name
- Visualize the interactions as a network graph
- Save and clear outputs

** Technologies Used
- Python
- Tkinter (GUI)
- pandas (planned)
- matplotlib + networkx (planned for visualization)

* Project Status
Current Progress: 30% (Initial Framework)**  
- GUI layout completed using Tkinter  
- Functional placeholders created for loading, predicting, visualizing, clearing, and saving

** Upcoming Features
- Implement interaction logic
- Graph-based network visualization
- Add scrollbars and filter options
- CSV file parsing and error handling

**How to Run
1. Clone the repository
2. Open `main.py` in your IDE
3. Run the script using Python 3
