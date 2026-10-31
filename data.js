export const EVENTOS = [
  {
    id: "e01", status: "upcoming",
    titulo: "Degustação de Tintos de Inverno",
    data: "2026-08-22", hora: "19:00",
    local: "Vinicolo, Cordeiro, RJ",
    vagas: 24, vagasRestantes: 9,
    descricao: "Uma noite guiada por quatro tintos da casa, com foco em Tannat e cortes de guarda. O Guilherme conduz a degustação explicando processo de vinificação e escolhas de safra.",
    preco: 95,
  },
  {
    id: "e02", status: "upcoming",
    titulo: "Manhã de Degustação com Pequenos Produtores",
    data: "2026-09-12", hora: "09:00",
    local: "Vinicolo — Cordeiro, RJ",
    vagas: 40, vagasRestantes: 22,
    descricao: "Uma manhã de degustação guiada por rótulos que a Vinicolo selecionou entre pequenos produtores parceiros, com histórias sobre cada vinho e cada região. Atividade para toda a família.",
    preco: 120,
  },
  {
    id: "e03", status: "past",
    titulo: "Jantar Harmonizado — Inverno 2025",
    data: "2025-07-18", hora: "20:00",
    local: "Vinicolo, Cordeiro, RJ",
    descricao: "Cinco tempos harmonizados com a linha de tintos de guarda, em parceria com um chef local. Encerramos com o Tannat Concentrado e queijos maturados.",
  },
  {
    id: "e04", status: "past",
    titulo: "Degustação às Cegas",
    data: "2025-04-05", hora: "18:30",
    local: "Vinicolo, Cordeiro, RJ",
    descricao: "Convidados degustaram seis rótulos sem saber os rótulos, comparando notas com a equipe da loja. O tinto mais votado foi o Corte Serra Alta.",
  },
  {
    id: "e05", status: "past",
    titulo: "Expo Cordeiro 2026",
    data: "2026-07-11", hora: "todo o período da feira (11 a 19 de julho)",
    local: "Expo Cordeiro, Cordeiro, RJ",
    descricao: "A Vinicolo participou da 82ª Expo Cordeiro, uma das maiores exposições agropecuárias do Brasil (desde 1921), com entrada gratuita. Além de expor rótulos e receber visitantes para degustação, a Vinicolo ajudou a batizar a 'Alameda Quintal do Mundo', um dos espaços da feira.",
  },
];

export const POSTS = [
  {
    id: "b01", categoria: "Notas de Degustação",
    titulo: "Por que o Tannat é a alma dos tintos gaúchos",
    resumo: "Uma casta pouco conhecida fora do Brasil e do Uruguai, mas responsável por alguns dos tintos mais estruturados da Serra Gaúcha.",
    data: "2026-07-28", leitura: "6 min",
    corpo: "O Tannat chegou ao Rio Grande do Sul importado do sudoeste da França, mas encontrou aqui um solo e um clima que realçam sua estrutura tânica sem perder frescor. É uma uva difícil: casca espessa, taninos agressivos quando jovem, e uma exigência de manejo cuidadoso na vinha. Quando bem trabalhado, o resultado é um tinto de cor intensa, taninos firmes e um potencial de guarda que poucas castas locais alcançam. Na Vinicolo, usamos o Tannat como espinha dorsal dos nossos cortes de guarda e também em versão varietal concentrada, para quem quer conhecer a uva sem meio-termo."
  },
  {
    id: "b02", categoria: "Harmonização",
    titulo: "Espumante não é só para brinde: guia rápido de harmonização",
    resumo: "O espumante brasileiro método Charmat merece um lugar na mesa do dia a dia, não só nas comemorações.",
    data: "2026-07-14", leitura: "5 min",
    corpo: "Existe uma ideia enraizada de que espumante é bebida de ocasião especial. Na prática, a acidez e as bolhas fazem dele um dos vinhos mais versáteis para harmonizar com comida. Um Brut Charmat bem feito corta a gordura de frituras, refresca pratos com temperos fortes e acompanha desde um sushi até um queijo coalho na chapa. Já o rosé espumante tem corpo suficiente para ir de um brunch de fim de semana a uma sobremesa leve com frutas vermelhas. A dica da casa: sirva sempre bem gelado, entre 6°C e 8°C, e não guarde a garrafa aberta por mais de dois dias, mesmo na geladeira."
  },
  {
    id: "b03", categoria: "Bastidores da Vinícola",
    titulo: "Uma tarde de prova às cegas com o Guilherme",
    resumo: "Antes de qualquer rótulo novo chegar ao catálogo, ele passa pela mesa de prova — sem rótulo, sem preço, sem produtor.",
    data: "2026-06-30", leitura: "6 min",
    corpo: "Toda semana, algumas garrafas novas chegam à sala de degustação da Vinicolo para avaliação. O Guilherme prova cada uma às cegas: taças numeradas, sem informação sobre produtor ou preço, só o vinho. Ele anota cor, aroma, estrutura e final de boca antes de olhar qualquer ficha técnica. Só depois da nota fechada é que os dados comerciais entram na conversa — porque um vinho caro com nota baixa não entra no catálogo, e um vinho barato com nota alta é exatamente o tipo de descoberta que a Vinicolo quer colocar na sua mesa."
  },
  {
    id: "b04", categoria: "Notas de Degustação",
    titulo: "Chardonnay em barrica: o que a madeira realmente faz",
    resumo: "Amanteigado, tostado, cremoso — entendendo o que a passagem por barril acrescenta (e o que pode estragar).",
    data: "2026-06-16", leitura: "5 min",
    corpo: "Passar um Chardonnay por barrica de carvalho não é sobre 'dar sabor de madeira' — é sobre textura. O contato com a madeira microoxigena o vinho lentamente, suavizando a acidez e criando aquela sensação cremosa na boca. Notas de manteiga e vanilla vêm da fermentação e do próprio carvalho, mas em doses pequenas: barrica em excesso mascara a fruta e deixa o vinho pesado. No Chardonnay Barrica que selecionamos para o catálogo, a passagem é curta e parcial, só o suficiente para dar corpo sem perder a acidez que faz esse branco combinar com peixe."
  },
  {
    id: "b05", categoria: "Harmonização",
    titulo: "O que servir com churrasco além do tinto de sempre",
    resumo: "Cabernet com picanha todo mundo já sabe. Aqui vão três combinações menos óbvias para o próximo churrasco.",
    data: "2026-05-29", leitura: "4 min",
    corpo: "Churrasco brasileiro pede tinto estruturado, isso é quase consenso. Mas vale variar: um Tannat concentrado combina especialmente bem com cortes mais gordos, como costela, porque os taninos cortam a gordura. Para linguiça e embutidos temperados, um corte com Merlot suaviza o toque picante sem competir. E se a churrasqueira tiver frango e queijo coalho, um Rosé bem gelado entra como opção mais leve, para quem não quer só tinto pesado do início ao fim da tarde."
  },
  {
    id: "b06", categoria: "Bastidores da Vinícola",
    titulo: "Como o Guilherme escolhe os vinhos que entram no catálogo",
    resumo: "Nem todo rótulo que passa pela prova do Guilherme chega até você. Veja o que pesa nessa decisão.",
    data: "2026-05-08", leitura: "4 min",
    corpo: "Toda semana chegam amostras de rótulos novos para avaliação. O Guilherme prova cada um às cegas, sem saber preço ou produtor, e só depois de decidir se o vinho entra no catálogo é que os dados comerciais entram na conversa. O critério principal é simples: o vinho precisa entregar mais do que promete pelo preço que custa. Depois de aprovado, cada rótulo ganha sua ficha técnica completa — uva, região, safra e sugestão de harmonização — para que quem compra saiba exatamente o que está levando, não só o nome do rótulo."
  },
];
