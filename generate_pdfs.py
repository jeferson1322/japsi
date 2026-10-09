from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os

# Dados do profissional e valores
PROF = {
    'nome': 'Jeferson Alberto da Silva',
    'crp': '07/32502',
    'telefone': '47 99868-7400',
    'email': 'jehalberto@gmail.com'
}

VALORES = {
    'pacote5': 'R$ 1.200',
    'pacote10': 'R$ 2.200',
    'mensal': 'R$ 6.000/mês (até 10 atendimentos)',
    'plantao': 'R$ 250/hora',
    'palestra': 'R$ 1.200'
}

OUT_DIR = os.path.dirname(__file__)


def make_proposta(path):
    c = canvas.Canvas(path, pagesize=A4)
    w, h = A4
    margin = 20 * mm
    x = margin
    y = h - margin

    c.setFont('Helvetica-Bold', 16)
    c.drawString(x, y, 'Proposta de Programa de Apoio Psicológico para Colaboradores')
    y -= 12 * mm

    c.setFont('Helvetica', 11)
    c.drawString(x, y, f'Profissional: {PROF["nome"]}  |  CRP: {PROF["crp"]}')
    y -= 7 * mm
    c.drawString(x, y, f'Contato: {PROF["telefone"]}  |  {PROF["email"]}')
    y -= 10 * mm

    c.setFont('Helvetica-Bold', 12)
    c.drawString(x, y, 'Objetivo:')
    y -= 6 * mm
    c.setFont('Helvetica', 11)
    text = c.beginText(x, y)
    text.textLines('Oferecer atendimento psicológico clínico confidencial a colaboradores, com foco em promoção da saúde mental, redução de absenteísmo e suporte em situações de estresse e crise.')
    c.drawText(text)
    y = text.getY() - 8 * mm

    c.setFont('Helvetica-Bold', 12)
    c.drawString(x, y, 'Serviços incluídos:')
    y -= 6 * mm
    c.setFont('Helvetica', 11)
    services = [
        'Triagem inicial: entrevista breve para priorização.',
        'Atendimentos individuais: presencial ou online, com sigilo profissional.',
        'Plantão de crise: atendimento emergencial (opcional).',
        'Palestras/workshops: opcionais (tema e duração negociáveis).',
        'Relatórios agregados e anônimos para RH.'
    ]
    for s in services:
        c.drawString(x+6*mm, y, '- ' + s)
        y -= 6 * mm

    y -= 4 * mm
    c.setFont('Helvetica-Bold', 12)
    c.drawString(x, y, 'Pacotes e valores (ilustrativos):')
    y -= 8 * mm
    c.setFont('Helvetica', 11)
    c.drawString(x+4*mm, y, f'Pacote 5 sessões: {VALORES["pacote5"]} por vaga')
    y -= 6 * mm
    c.drawString(x+4*mm, y, f'Pacote 10 sessões: {VALORES["pacote10"]} por vaga')
    y -= 6 * mm
    c.drawString(x+4*mm, y, f'Contrato mensal: {VALORES["mensal"]}')
    y -= 6 * mm
    c.drawString(x+4*mm, y, f'Plantão de crise: {VALORES["plantao"]}')
    y -= 6 * mm
    c.drawString(x+4*mm, y, f'Palestra/workshop: {VALORES["palestra"]}')
    y -= 10 * mm

    c.setFont('Helvetica-Bold', 12)
    c.drawString(x, y, 'Confidencialidade e ética:')
    y -= 6 * mm
    c.setFont('Helvetica', 11)
    text = c.beginText(x, y)
    text.textLines('Atendimentos com sigilo profissional. Relatórios ao RH somente com dados agregados e não identificáveis. Consentimento informado assinado pelo colaborador. Adequação à LGPD e normas do CRP.')
    c.drawText(text)
    y = text.getY() - 10 * mm

    c.setFont('Helvetica-Bold', 12)
    c.drawString(x, y, 'Condições comerciais:')
    y -= 6 * mm
    c.setFont('Helvetica', 11)
    c.drawString(x+4*mm, y, 'Prazo de validade: 30 dias. Pagamento: 50% adiantado, 50% ao término do pacote (negociável). Política de faltas: reagendamento com 24h de antecedência.')

    c.showPage()
    c.save()


def make_folheto(path):
    c = canvas.Canvas(path, pagesize=A4)
    w, h = A4
    margin = 20 * mm
    x = margin
    y = h - margin

    c.setFont('Helvetica-Bold', 20)
    c.drawString(x, y, 'Apoio Psicológico para Colaboradores')
    y -= 16 * mm

    c.setFont('Helvetica', 12)
    c.drawString(x, y, 'Atendimento clínico confidencial (presencial ou online)')
    y -= 10 * mm

    c.setFont('Helvetica-Bold', 13)
    c.drawString(x, y, 'Pacotes')
    y -= 8 * mm
    c.setFont('Helvetica', 12)
    c.drawString(x, y, f'• Pacote 5 sessões: {VALORES["pacote5"]}')
    y -= 7 * mm
    c.drawString(x, y, f'• Pacote 10 sessões: {VALORES["pacote10"]}')
    y -= 7 * mm
    c.drawString(x, y, f'• Contrato mensal: {VALORES["mensal"]}')
    y -= 12 * mm

    c.setFont('Helvetica-Bold', 13)
    c.drawString(x, y, 'Serviços Disponíveis')
    y -= 8 * mm
    c.setFont('Helvetica', 12)
    lines = ['Triagem inicial', 'Atendimentos individuais', 'Plantão de crise', 'Palestras e workshops', 'Relatórios agregados (anônimos)']
    for ln in lines:
        c.drawString(x+4*mm, y, '• ' + ln)
        y -= 7 * mm

    y -= 8 * mm
    c.setFont('Helvetica-Bold', 12)
    c.drawString(x, y, 'Contato')
    y -= 7 * mm
    c.setFont('Helvetica', 12)
    c.drawString(x, y, f'{PROF["nome"]}  |  CRP {PROF["crp"]}')
    y -= 6 * mm
    c.drawString(x, y, f'Tel: {PROF["telefone"]}  |  {PROF["email"]}')

    c.showPage()
    c.save()


if __name__ == '__main__':
    proposta_path = os.path.join(OUT_DIR, 'Proposta_Apoio_Psicologico_Jehalberto.pdf')
    folheto_path = os.path.join(OUT_DIR, 'Folheto_Apoio_Psicologico_Jehalberto.pdf')
    make_proposta(proposta_path)
    make_folheto(folheto_path)
    print('PDFs gerados:')
    print(proposta_path)
    print(folheto_path)
