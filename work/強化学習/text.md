# わかったことをまとめていく

### 強化学習の基本的な枠組み
+ エージェント、環境、及それらの間の相互作用からなる
	+ エージェントは、行動決定が主体
	+ 環境は、エージェントが相互作用を行う対象
	+ 相互作用とは、情報の受け渡しを行うこと
+ 相互作用の数理モデル
	+ マルコフ決定過程(MDP)が基本
		+ エージェントと環境は、1時間ステップごとに、状態、行動、報酬という三つの情報(編集)を受け取ったり、引き渡したりする
		+ 図としては、ループ構造を形成している
	+ 部分観測マルコフ決定過程
		+ エージェントが状態を直接受け取ることができない

+ 基本的な三つの変数
	+ 状態
		+ エージェントが置かれている状況を表す
	+ 行動
		+ エージェントが環境に対して行う働きかけの種類
	+ 報酬
		+ その行動の即時的な良さを表す

