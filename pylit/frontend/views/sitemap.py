from flask import Blueprint, render_template, current_app, url_for

sitemap_blueprint = Blueprint('sitemap', 'pylit')

@sitemap_blueprint.route('/sitemap')
def site_map():
    links=[]
    for rule in current_app.url_map.iter_rules():
        endpoint = rule.endpoint
        try:
            url = url_for(rule.endpoint)
            if not url.startswith('/_debug'):
                links.append((url, rule.endpoint))
        except:
            pass
    return render_template('sitemap.jinja', links=links)
