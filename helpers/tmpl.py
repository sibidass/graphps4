from string import Template


'''Stores all output templates'''

sheader = "---------Function $func----------"

show_all = "Total no. of freight trains: $tcount\n" \
           "Total no. of cities: $ccount\n" \
           "List of Freight trains:\n" \
           "$train_list\n" \
           "List of cities:\n" \
           "$city_list\n\n"

display_transport_hub = "Main transport hub: $hub\n" \
                        "Number of trains visited: $tcount\n" \
                        "List of Freight trains:\n" \
                        "$train_list\n\n"

display_connected_cities = "Freight train number: $train_no\n" \
                           "Number of cities connected: $ccount\n" \
                           "List of cities connected directly by $train_no:\n" \
                           "$city_list\n\n"

transit_details = "City A: $src\n" \
                   "City B: $dest\n" \
                   "$msg\n\n"

class LoadTemplates:
    def __init__(self, **kwargs):
        self.tmplts = self.load_template(**kwargs)

    def load_template(self, **kwargs):
        tmplts = {}
        for k, v in kwargs.items():
            tmplts[k] = Template(v)
        return tmplts

    def show(self, tmpl, **kws):
        return self.tmplts[tmpl].substitute(**kws)


loaded_templates = LoadTemplates(show_all=show_all, section_header=sheader, t_hub=display_transport_hub,
                                 cc=display_connected_cities, d_transit=transit_details)
