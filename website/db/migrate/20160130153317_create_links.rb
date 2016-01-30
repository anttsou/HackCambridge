class CreateLinks < ActiveRecord::Migration
  def change
    create_table :links do |t|
      t.string "url", :null => false
      t.text "raw", :limit => 4294967295
      t.timestamps
    end
  end
end
