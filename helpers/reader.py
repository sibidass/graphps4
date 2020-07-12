def file_reader(filename):
    print("reading file {}".format(filename))
    train_details = {}
    with open(filename) as f:
        for line in f:
            train = line.split("/")[0].strip()
            cities = [c.strip().strip("\n") for c in line.split("/")[1:]]
            train_details[train] = cities
    return train_details

def file_writer(filename, *args):
    text = "\n".join(args)
    with open(filename, "a") as f:
        f.write(text)

def read_prompts(filename):
    with open(filename) as f:
        return f.readlines()