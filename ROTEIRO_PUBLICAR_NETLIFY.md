# Roteiro: publicar o site no Netlify

Este roteiro explica como publicar o site e obter um link público gratuito com o endereço `netlify.app`.

## 1. Conferir os arquivos

Confirme que a pasta do site contém o arquivo `index.html` e os demais arquivos usados pela página. Não é necessário gerar uma compilação: este projeto é um site estático.

## 2. Criar ou acessar uma conta

1. Acesse [app.netlify.com](https://app.netlify.com/).
2. Entre na sua conta ou crie uma conta gratuita.

## 3. Publicar a pasta

1. Abra [app.netlify.com/drop](https://app.netlify.com/drop/).
2. Arraste para a página a pasta do projeto que contém o `index.html`.
3. Aguarde o Netlify terminar a publicação.

Se o navegador não aceitar a pasta inteira, compacte os arquivos do site em um `.zip` e envie o arquivo compactado.

## 4. Abrir e compartilhar o link

Depois da publicação, o Netlify mostrará um endereço parecido com:

```text
https://nome-aleatorio.netlify.app
```

Abra esse endereço para conferir o site. Se estiver correto, esse é o link que você pode compartilhar.

## 5. Personalizar o endereço gratuito (opcional)

No painel do site no Netlify, procure as configurações de domínio do site e altere o nome gerado para outro nome disponível. O endereço continuará terminando em `.netlify.app`.

## Atualizar o site depois

Quando fizer alterações nos arquivos, publique novamente a pasta atualizada pelo Netlify Drop ou conecte um repositório GitHub ao site para automatizar as próximas publicações.

## Usar um domínio próprio (opcional)

Um domínio próprio, como `www.seudominio.com`, é diferente do endereço gratuito `netlify.app` e pode exigir a compra do domínio e a configuração do DNS. O arquivo `CNAME` deste projeto ainda contém `www.seu-dominio.com`, que é um exemplo: não o use como se fosse o endereço real do site.

## Conferência final

- Abra o link público em uma janela anônima ou em outro dispositivo.
- Confira se imagens, botões e links estão funcionando.
- Compartilhe o link `netlify.app` somente depois dessa conferência.