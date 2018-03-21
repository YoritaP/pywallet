from pywallet import wallet

#key
wallet_key = ["coin", "seed", "address", "wif", "public_key", "xpublic_key", "xpublic_key_prime","private_key", "xprivate_key"] # +"children"
child_key = ["path", "bip32_path", "address", "xpublic_key"]

# generate children num
wallet_children = 5
# generate 12 word mnemonic seed
seed = wallet.generate_mnemonic()

# create bitcoin wallet
wal = wallet.create_wallet(network="BTC", seed=seed, children=wallet_children)

if __name__ == '__main__':
    for dic in wallet_key:
        print(dic + " : " + str(wal[dic]))
    for child in range(wallet_children):
        print("  child : " + str(child))
        for dic in child_key:
            print("    " + dic + " : " + str(wal["children"][child][dic]))
