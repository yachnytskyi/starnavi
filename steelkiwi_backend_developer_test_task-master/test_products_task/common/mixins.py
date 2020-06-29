from braces.views import AjaxResponseMixin, JSONResponseMixin


class AjaxFormViewMixin(AjaxResponseMixin, JSONResponseMixin):

    def form_invalid(self, form) :
        return self.render_json_response(form.errors, status=400)
        # if self.request.is_ajax():
        #     return self.render_json_response(form.errors, status=400)
        # return super(AjaxResponseMixin, self).form_invalid(form)


class ActiveTabMixin(object):
    active_tab = 'default'

    def get_context_data(self, **kwargs):
        context = super(ActiveTabMixin, self).get_context_data(**kwargs)
        context['active_tab'] = self.active_tab
        return context
