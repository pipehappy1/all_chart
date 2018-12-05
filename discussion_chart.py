def read_data(data_file):
    host_count = {}
    clerk_count = {}
    member_count = {}
    all_count = {}
    with open(data_file, 'r') as fh:
        for line in fh:
            line = line.strip()
            if len(line) == 0:
                continue
            if line[0] == "#":
                continue
            else:
                items = line.split(',')
                date = items[0]
                host = items[1]
                clerk = items[2]
                members = items[3]
                if host not in host_count:
                    host_count[host] = 1
                else:
                    host_count[host] = host_count[host] + 1

                if clerk not in clerk_count:
                    clerk_count[clerk] = 1
                else:
                    clerk_count[clerk] = clerk_count[clerk] + 1

                member_items = members.split(';')
                for member in member_items:
                    if len(member) > 0:
                        if member not in member_count:
                            member_count[member] = 1
                        else:
                            member_count[member] = member_count[member] + 1

                appearance = {}
                appearance[host] = 1
                appearance[clerk] = 1
                for member in member_items:
                    if len(member) > 0:
                        appearance[member] = 1
                for m in appearance.keys():
                    if m not in all_count:
                        all_count[m] = 1
                    else:
                        all_count[m] = al_count[m] + 1


        print(host_count)
        print(clerk_count)
        print(member_count)
    host_by_attendence = sorted(host_count.items(), key=lambda kv: kv[1])
    clerk_by_attendence = sorted(clerk_count.items(), key=lambda kv: kv[1])
    member_by_attendence = sorted(member_count.items(), key=lambda kv: kv[1])
    all_by_attendence = sorted(all_count.items(), key=lambda kv: kv[1])
    host_by_attendence.reverse()
    clerk_by_attendence.reverse()
    member_by_attendence.reverse()
    all_by_attendence.reverse()
    print(host_by_attendence)
    print(clerk_by_attendence)
    print(member_by_attendence)
    print(all_by_attendence)
    return host_by_attendence, clerk_by_attendence, member_by_attendence, all_by_attendence


def write_chart(save_name, host_by_attendence, clerk_by_attendence, member_by_attendence, all_by_attendence):
    pass


def draw_chart(data_file, save_name):
    host_by_attendence, clerk_by_attendence, member_by_attendence, all_by_attendence = read_data(data_file)
    write_chart(save_name, host_by_attendence, clerk_by_attendence, member_by_attendence, all_by_attendence)
    

if __name__ == "__main__":
    data_file = "/Users/yguan/workspace/papers/MOST/student_issue/discussion_record.csv"
    draw_chart(data_file, './example.jpg')
