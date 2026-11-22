# Changelog

## 日本語対応

### 変更点
- `src/i18n_ja.py` 追加: メイン UI・チュートリアル・領域ペイント・フルシェイプ入出力の日本語訳。
- `src/text/i18n_ja.py` 追加: テキストタブの日本語訳。
- `src/i18n.py` / `src/text/i18n_locales.py`: 上記を `"ja"` として登録。
- `src/app.py`: 言語選択に「日本語」を追加し、起動時の既定言語を日本語に変更 (`DEFAULT_LANGUAGE`)。残り時間表示の接尾辞「残り」を追加。

英語の全キー (383) を翻訳済み。プレースホルダー (`{count}` 等) は英語版と一致。

### 用語
| 英語 | 日本語 |
|---|---|
| Vinyl | バイナル (ゲーム内表記に準拠) |
| Vinyl Group Editor | バイナルグループエディター |
| layer | レイヤー |
| template | テンプレート |
| ungroup | グループ解除 |
| full-shape | フルシェイプ |
| Region Paint | 領域ペイント |
| first pass | 初回パス |

### 未対応・懸念点
- ゲーム内の日本語 UI 表記と未照合。用語は要確認。
- メイン UI のフォントは `"Segoe UI"` 固定 (`ui_font_name` はメイン UI では未使用。`text/ui/char_grid_picker.py` のみで使用)。日本語は Windows のフォントリンクで表示されるが、游ゴシック UI 等への切替は未実施。
- `tr()` を通らないハードコード文字列 (ログ、例外メッセージ等) は英語のまま。
- レビューで pytest 155 件の通過と、日本語既定での起動を確認済み。日本語フォント表示の目視確認と FH6 実機でのインポートは未実施。
- 日本語既定でも英語のまま残る表示 (派生元のコード起因):
  - 品質プロファイルの説明 (`config/settings/*.ini` の description)。対応は保留。
  - (修正済み) 領域ペイントのステータス "Ready" をハードコードしていた。`tr(self.lang, "ready")` に変更。言語切替時には更新されない (起動時の言語で固定)。
  - (修正済み) テキストタブのラベルにキー名 `text_layer_estimate_idle` がそのまま表示されていた。en/ja にキーを追加し、`tests/test_i18n_keys.py` で検証。
  - `text_layer_estimate_working` も en に無いが、画面に表示されない StringVar にのみ使われるため未対応。

## README 日本語版

### 変更点
- `README.ja-JP.md` 追加: `README.md` (v1.9.6) の全文訳。変更履歴も含む。冒頭に派生版である旨を追記。
- `README.md`: 言語リンクに「日本語」を追加。

### 未対応・懸念点
- アプリ操作名は日本語 UI 文字列 (`src/i18n_ja.py` 等) に合わせた。UI 訳を変えた場合は README も要更新。
- ゲーム内表記「バイナルグループの作成」「グループ解除」は未照合。
- ダウンロードリンクは派生元の Releases のまま (変更するかは保留)。本リポジトリのリリースは未作成で、派生元の EXE は英語が既定。
- 他言語の README (zh-CN / ko-KR / es-MX) は修正しない方針。

## 派生元 v1.9.7 の取り込み

### 変更点
- `main` (派生元 v1.9.7) を `feature/japanese-localization` にマージ。
- `src/app.py` の衝突を解消。派生元で追加された UI 言語の記憶を採用し、保存値が無い場合の既定を日本語にした。
- `src/ui_preferences.py`: `SUPPORTED_UI_LANGUAGES` に `"ja"` を追加。無いと保存した日本語が読み込み時に破棄され、毎回既定に戻る。`tests/test_ui_preferences.py` で検証。
- `src/i18n_ja.py`: 派生元の英語文字列の変更に追従 (追加 7、変更 2、削除 2)。キー数 389 で en と一致。
- `README.ja-JP.md`: v1.9.7 に追従 (バージョン、出力先 `out/`・`image/`、変更履歴)。

### 懸念点
- 派生元が今後 `SUPPORTED_UI_LANGUAGES` や `LANGUAGES` を変更すると、同様の衝突・取りこぼしが起きる。
