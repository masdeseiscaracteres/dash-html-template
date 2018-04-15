import dash_html_components as html
import lxml.html
from lxml.etree import XPath


class Template:
    @staticmethod
    def from_file(path, injection_dict=None):
        with open(path, 'r') as f:
            html_str = f.read()
        return Template.from_string(html_str, injection_dict)

    @staticmethod
    def from_string(html_str, injection_dict=None):
        e = lxml.html.fragment_fromstring(html_str)
        return _inject(e, injection_dict)


def _inject(elem, injection_dict=None):
    if isinstance(elem, str):
        return elem
    elif isinstance(elem, lxml.html.HtmlElement):
        c = _get_descendants(elem)
        contents = [_inject(x, injection_dict) for x in c]
        return _get_dash_component(elem.tag, elem.attrib, contents, injection_dict)


def _get_descendants(elem):
    """Obtain descendants including both text nodes and html tags"""
    f = XPath("child::node()")
    return f(elem)


def _get_dash_component(tag_name, attribs, children, injection_dict):
    # Convert from lxml Element to Dash
    component_name = tag_name.title()
    attrib_dict = _convert_attributes(dict(attribs))
    if component_name == 'Template':  # injection
        try:
            return injection_dict[attrib_dict['id']]  # replace the template element
        except (KeyError, TypeError):
            return getattr(html, component_name)(children, **attrib_dict)  # let the template tag go untouched
    else:
        return getattr(html, component_name)(children, **attrib_dict)


def _convert_attributes(attrib_dict):
    try:
        attrib_dict['className'] = attrib_dict.pop('class')
    except KeyError:
        pass
    try:
        attrib_dict['style'] = _convert_style(attrib_dict['style'])
    except KeyError:
        pass
    return attrib_dict


def _convert_style(elem_style):
    d = {}
    for x in elem_style.split(";"):
        if x:
            k, v = x.split(":")
            key = k.strip()  # TODO: should be camelCased. e.g. instead of text-align, it's textAlign
            d[key] = v.strip()
    return d
