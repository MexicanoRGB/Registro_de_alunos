#Sistema De Alunos
import os
import pandas as pd

CSV_FILE = 'alunos.csv'
CAMPOS = ['Matricula', 'Nome', 'Rua', 'Numero', 'Bairro', 'Cidade', 'UF', 'Telefone', 'Email']

def load_data():
    #le o cvs e cria dataframe
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=CAMPOS)
        df = df.astype({
        'Matricula': 'int64',
        'Nome': 'string',
        'Rua': 'string',
        'Numero': 'string',
        'Bairro': 'string',
        'Cidade': 'string',
        'UF': 'string',
        'Telefone': 'string',
        'Email': 'string'
        })
        return df
    df = pd.read_csv(CSV_FILE, dtype=str)
    # garante que as colunas existam
    for c in CAMPOS:
        if c not in df.columns:
            df[c] = ''
    df = df[CAMPOS]
    df['Matricula'] = df['Matricula'].fillna('').replace('', '0')
    df['Matricula'] = df['Matricula'].astype(int)
    return df

def save_data(df):#salva dataframe
    df.to_csv(CSV_FILE, index=False)
    
def generate_matricula(df):#gerador de matricula
    if df.empty:
        return 1
    max_mat = int(df['Matricula'].max())
    return max_mat + 1

def input_nonempty(prompt, default=None):
    texto = input(prompt).strip()
    if texto == '' and default is not None:
        return default
    return texto

def mostrar_aluno(reg):#exibe dados do aluno
    print('_'*40)
    print(f"Matrícula: {reg['Matricula']}")
    print(f"Nome : {reg['Nome']}")
    print(f"Rua : {reg['Rua']}")
    print(f"Número : {reg['Numero']}")
    print(f"Bairro : {reg['Bairro']}")
    print(f"Cidade : {reg['Cidade']}")
    print(f"UF : {reg['UF']}")
    print(f"Telefone : {reg['Telefone']}")
    print(f"E-mail : {reg['Email']}")
    print('-' * 40)

def inserir(df):#insere/cria novo aluno
    print('=== INSERIR NOVO ALUNO ===')
    matricula = generate_matricula(df)

    while True:
        nome = input('Nome: ').strip()
        if nome == '':
            print('Erro: Nome é obrigatório. Tente novamente.')
            continue
        if not any(char.isdigit() for char in nome):
            break
        else:
            print('Erro: O nome não pode conter números. Tente novamente.')
    
    while True:
        rua = input('Rua: ').strip()
        if rua == '':
            print('Erro: Rua é obrigatória. Tente novamente.')
            continue
        break
    
    while True:
        numero = input('Número: ').strip()
        if numero == '':
            print('Erro: Número é obrigatório. Tente novamente.')
            continue
        if numero.isdigit():
            break
        else:
            print('Erro: O número deve conter apenas dígitos. Tente novamente.')
    
    while True:
        bairro = input('Bairro: ').strip()
        if bairro == '':
            print('Erro: Bairro é obrigatório. Tente novamente.')
            continue
        break
    
    while True:
        cidade = input('Cidade: ').strip()
        if cidade == '':
            print('Erro: Cidade é obrigatória. Tente novamente.')
            continue
        break
    
    while True:
        uf = input('UF: ').strip()
        if uf == '':
            print('Erro: UF é obrigatório. Tente novamente.')
            continue
        break
    
    while True:
        telefone = input('Telefone: ').strip()
        if telefone == '':
            print('Erro: Telefone é obrigatório. Tente novamente.')
            continue
        if telefone.isdigit():
            break
        else:
            print('Erro: O telefone deve conter apenas dígitos. Tente novamente.')
    
    while True:
        email = input('E-mail: ').strip()
        if email == '':
            print('Erro: E-mail é obrigatório. Tente novamente.')
            continue
        break
    #essas coisas sao pra garantir que n tenha campo vazio
    registro = {
        'Matricula': int(matricula),
        'Nome': nome,
        'Rua': rua,
        'Numero': numero,
        'Bairro': bairro,
        'Cidade': cidade,
        'UF': uf,
        'Telefone': telefone,
        'Email': email
    }
    df2 = pd.concat([df, pd.DataFrame([registro])], ignore_index=True)
    df2['Matricula'] = df2['Matricula'].astype(int)
    save_data(df2)
    print(f'Aluno cadastrado com matrícula {matricula}.')
    return df2

def buscar_por_matricula(df, matricula):
    try:
        m = int(matricula)
    except ValueError:
        return pd.DataFrame()
    return df[df['Matricula'] == m]

def buscar_por_nome(df, nome):
    nome_proc = nome.strip().lower()
    mask = df['Nome'].str.lower().str.contains(nome_proc, na=False)
    return df[mask]

def pesquisar(df):
    print('=== PESQUISAR ALUNO ===')
    print('1 - Por Matrícula')
    print('2 - Por Nome')
    opc = input('Escolha uma opção (1-2): ').strip()
    if opc == '1':
        matricula = input_nonempty('Digite a matrícula: ')
        df_matches = buscar_por_matricula(df, matricula)
    elif opc == '2':
        nome = input_nonempty('Digite o nome (ou parte dele): ')
        df_matches = buscar_por_nome(df, nome)
    else:
        print('Opção inválida.')
        return df
    registro = escolher_registro(df_matches)
    if registro is None or registro.empty:
        print('Nenhum aluno selecionado.')
        return df
    
    mostrar_aluno(registro)
    df = editar_registro(df, registro)
        
    return df

def escolher_registro(df_matches):#escolhe registro entre 2 ou mais resultados
    if df_matches.empty:
        print('Nenhum registro encontrado.')
        return df_matches
    elif len(df_matches) == 1:
        return df_matches.iloc[0]
    print(f'{len(df_matches)} registros encontrados:')
    for _, r in df_matches.iterrows():
        print(f"Matrícula: {r['Matricula']} - Nome: {r['Nome']}")
    while True:
        escolha = input('Digite a matrícula do aluno que deseja selecionar (ou Enter para cancelar): ').strip()
        if escolha == '':
            return None
        sel = buscar_por_matricula(df_matches, escolha)
        if not sel.empty:
            return sel.iloc[0]
        print('Matrícula inválida para os resultados mostrados. Tente novamente.')

def editar_registro(df, registro):#só pra editar o registro de um aluno pqp
    if registro is None:
        print('Nenhum registro para editar.')
        return df
    resp = input('Deseja editar este registro? (s/n): ').strip().lower()
    mostrar_aluno(registro)
    if resp != 's':
        return df
    campos_editaveis = [c for c in CAMPOS if c != 'Matricula']
    while True:
        print('Campos editáveis:')
        for i, c in enumerate(campos_editaveis, start=1):
            print(f'{i} - {c}')
        print('0 - Sair da edição')
        print('R - Remover registro')
        escolha = input('Escolha o campo que deseja editar (0 para sair): ').strip().lower()
        
        if escolha == 'r':
            # opção para remover
            mostrar_aluno(registro)
            resp_remover = input('Deseja remover este registro? (s/n): ').strip().lower()
            if resp_remover == 's':
                df2 = df[df['Matricula'] != int(registro['Matricula'])]
                save_data(df2)
                print('Registro removido.')
                return df2
            else:
                print('Remoção cancelada.')
                continue
        
        if escolha == '0':
            break
        try:
            idx = int(escolha) - 1
            if idx < 0 or idx >= len(campos_editaveis):
                raise ValueError
        except ValueError:
            print('Opção inválida. Tente novamente.')
            continue
        campo = campos_editaveis[idx]
        valor_atual = registro[campo]
        novo = input_nonempty(f'Valor atual ({campo}) = "{valor_atual}". Novo valor (Enter = manter): ', default=valor_atual)
        df.loc[df['Matricula'] == registro['Matricula'], campo] = novo
        registro = df[df['Matricula'] == int(registro['Matricula'])].iloc[0]
        print(f'Campo "{campo}" atualizado.')
    save_data(df)
    print('Edição finalizada e salva.')
    return df

def remover_registro(df, registro):
    if registro is None:
        print('Nenhum registro para remover.')
        return df
    mostrar_aluno(registro)
    resp = input('Deseja remover este registro? (s/n): ').strip().lower()
    if resp != 's':
        print('Remoção cancelada.')
        return df
    df2 = df[df['Matricula'] != int(registro['Matricula'])]
    save_data(df2)
    print('Registro removido.')
    return df2

def main():
    df = load_data()
    while True:
        print('\n=== MENU PRINCIPAL ===')
        print('1 - INSERIR')
        print('2 - PESQUISAR')
        print('3 - SAIR')
        opc = input('Escolha uma opção (1-3): ').strip()
        if opc == '1':
            df = inserir(df)
        elif opc == '2':
            df = pesquisar(df)
        elif opc == '3':
            print('Saindo do sistema. Até logo!')
            break
        else:
            print('Opção inválida. Tente novamente.')
if __name__ == "__main__":
    main()