{{- define "securecart.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}
