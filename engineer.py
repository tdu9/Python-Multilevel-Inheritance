class Engineer:
    def __init__(self, license_no):
        self.license_no = license_no
    def design_project(self):
        print('I am designing a project')

class SeniorEngineer(Engineer):
    def __init__(self, license_no, num_projects):
        super().__init__(license_no)
        self.num_projects = num_projects
    def deal_project(self):
        print('I have a project to do')
        self.num_projects += 1

class SeniorComputerEngineer(SeniorEngineer):
    def __init__ (self, license_no, num_projects, current_project):
        super().__init__(license_no, num_projects)
        self.current_project = current_project

leslie = Engineer('AB1234')
leslie.design_project()

cindy = SeniorEngineer('MN5678', 4)
cindy.deal_project()
print('Now Cindy has handled ' + str(cindy.num_projects) + ' projects.')

terry = SeniorComputerEngineer('PQ3456', 6, 'network connection')
print(terry.current_project)

        
    

