from bs4 import BeautifulSoup


def html_to_json_purser(new_file):
    # rss and atom feeds categorized by there type.I found from internet 8 custom feed types which I can use in project
    rss_feed_links_attributes = ['application/rss+xml', 'application/rss', 'text/rss+xml', 'text/rss']
    atom_feed_links_attributes = ['application/atom+xml', 'application/atom', 'text/atom+xml', 'text/atom']
    # parsing html file
    soup = BeautifulSoup(new_file.read(), "html.parser")
    rss_link = []
    rss_a = []
    atom_link = []
    atom_a = []
    # Finds all existing <a> tags which has attribute href
    for a in soup.find_all('a', href=True):
        if a.has_attr('type'):
            # if type of attribute one of the rss_feed_links_attributes then add the link value to the rss_a array
            if a['type'] in rss_feed_links_attributes:
                rss_a.append(a['href'])
            # else if type of attribute one of the atom_feed_links_attributes then add the link value to  atom_a array
            elif a['type'] in atom_feed_links_attributes:
                atom_a.append(a['href'])
    # Same things repeating for the <link> tag
    for link in soup.find_all('link', href=True):
        if link.has_attr('type'):
            if link['type'] in rss_feed_links_attributes:
                rss_link.append(link['href'])
            elif link['type'] in atom_feed_links_attributes:
                atom_link.append(link['href'])
    # after finding both of the link I concatenate both of them
    new_rss_list = rss_a + rss_link
    new_atom_list = atom_a + atom_link
    # adding both values to the dictionary which will return as value of function
    output_dictionary = {'rss': new_rss_list, 'atom': new_atom_list}
    return output_dictionary


