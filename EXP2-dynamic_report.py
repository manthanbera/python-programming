# Dynamic report generator (Experiment 2)

def bold_text(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "**" + result + "**"
    return wrapper

class report:
    templates = {}

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, func):
        cls.templates[name] = func
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    def __call__(self, template_name):
        template = self.templates.get(template_name)
        if template:
            return template(self.title, self.content)
        return self.title + ": " + self.content

    def __str__(self):
        return self.title + ": " + self.content


def simple_template(title, content):
    return title + ": " + content
@bold_text
def fancy_template(title, content):
    return title + ": " + content

def main():
    report.add_template("simple", simple_template)
    report.add_template("fancy", fancy_template)

    report = report("Sales Report", "Total sales: $5000")

    print("Simple Report:")
    print(report("simple"))

    print("\nFancy Report:")
    print(report("fancy"))

    print("\nDefault Report:")
    print(report)

if __name__ == "__main__":
    main()
