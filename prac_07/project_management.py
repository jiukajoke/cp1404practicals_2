import datetime
from project import Project


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]  # Skip the header line
            for line in lines:
                fields = line.strip().split('\t')
                name, start_date, priority, estimate, completion = fields
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
                priority = int(priority)
                estimate = float(estimate)
                completion = int(completion)
                project = Project(name, start_date, priority, estimate, completion)
                projects.append(project)
    except FileNotFoundError:
        pass
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        # Write the header line
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    incomplete_projects.sort(key=lambda x: x.priority)
    completed_projects.sort(key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date_filter):
    date_filter = datetime.datetime.strptime(date_filter, "%d/%m/%Y").date()
    filtered_projects = [project for project in projects if project.start_date > date_filter]
    filtered_projects.sort(key=lambda x: x.start_date)

    for project in filtered_projects:
        print(f"{project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))

    project = Project(name, start_date, priority, estimate, completion)
    projects.append(project)


def update_project(projects):
    for idx, project in enumerate(projects):
        print(f"{idx} {project}")
    choice = int(input("Project choice: "))
    if 0 <= choice < len(projects):
        project = projects[choice]
        new_completion = input("New Percentage (leave blank to retain existing): ")
        new_priority = input("New Priority (leave blank to retain existing): ")
        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
    else:
        print("Invalid project choice!")


if __name__ == "__main__":
    projects_file = "projects.txt"
    projects = load_projects(projects_file)

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_filter = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_filter)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")