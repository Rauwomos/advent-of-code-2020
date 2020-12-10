from day_7.bag import Bag

if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        raw_input = list(map(lambda x: x.strip(), f.readlines()))
    bags = Bag.create_bags(raw_input)
    print(bags['shiny gold'].get_descendant_count())